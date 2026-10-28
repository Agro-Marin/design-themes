from odoo import models
from odoo.http import request
from odoo.tools.test_runtime import get_test_runtime


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _pre_dispatch(cls, rule, args):
        # Allow public user to use `fw` query string in test mode to ease tests
        force_website_id = request.httprequest.args.get("fw")
        if get_test_runtime().is_running() and force_website_id:
            request.env["website"]._force_website(force_website_id)

        super()._pre_dispatch(rule, args)
