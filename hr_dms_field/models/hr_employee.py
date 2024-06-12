# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def write(self, vals):
        """When modifying a record that has linked directories and changing the
        user_id field it is necessary to update the auto-generated access group
        (name and explicit_user_ids).
        """
        res = super().write(vals)
        for item in self.filtered("dms_directory_ids"):
            if "user_id":
                template = self.env["dms.field.template"]._get_template_from_model(
                    item._name
                )
                if template:
                    template._get_autogenerated_group(item)
        return res

    def unlink(self):
        """When deleting a record, we also delete the linked directories and the
        auto-generated access group.
        """
        for record in self.filtered("dms_directory_ids"):
            group = self.env["dms.access.group"]._get_item_from_dms_field_ref(record)
            record.sudo().dms_directory_ids.unlink()
            group.sudo().unlink()
        return super().unlink()
