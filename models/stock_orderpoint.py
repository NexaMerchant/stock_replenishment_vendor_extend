from odoo import models, fields, api


class StockWarehouseOrderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    vendor_id = fields.Many2one(
        "res.partner",
        string="Preferred Vendor",
        domain="[('supplier_rank', '>', 0)]",
        help="Manually set a preferred vendor to be used when replenishing this product."
    )

    def _prepare_orderpoint_procurement(self):
        vals = super()._prepare_orderpoint_procurement()
        if self.vendor_id:
            vals['partner_id'] = self.vendor_id.id
        return vals
