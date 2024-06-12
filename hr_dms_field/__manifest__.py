# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Add dms field for employees",
    "version": "15.0.1.2.0",
    "category": "Human Resources",
    "website": "https://github.com/OCA/dms",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["hr", "dms_field"],
    "installable": True,
    "data": ["views/hr_employee_view.xml"],
    "demo": ["demo/dms_data.xml"],
    "assets": {
        "web.assets_backend": [
            "hr_dms_field/static/src/js/**/*",
        ],
    },
    "maintainers": ["victoralmau"],
}
