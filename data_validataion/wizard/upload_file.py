from odoo import models, fields, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError
import pandas as pd

from collections import defaultdict


class ImportFileWizard(models.TransientModel):
    _name = "import.file.wizard"
    file = fields.Binary(string="File", required=True)

    def upload_file(self):
        configs = self.env["config.data"].search([])
        config_data = defaultdict(
            lambda: {
                "field": False,
                "is_nullable": False,
                "is_unique": False,
                "allow_formula": False,
            }
        )
        for config in configs:
            config_data[config.name] = {
                "field": config.field,
                "is_nullable": config.is_nuallable,
                "is_unique": config.is_unique,
                "allow_formula": config.allow_formula,
            }
        wb = openpyxl.load_workbook(
            filename=BytesIO(base64.b64decode(self.file)), read_only=True
        )
        file_content = base64.b64decode(self.file)
        df = pd.read_excel(BytesIO(file_content))
        # if "No." in df.columns:
        #     no_column = df["No."]            
        #     print("No column data:", no_column.tolist())
        for key, value in config_data.items():
            key_string = str(key)
            key_column = df[key_string]   
            print("No column data:", key_column.tolist())


