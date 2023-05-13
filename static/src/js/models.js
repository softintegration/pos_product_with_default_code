odoo.define('pos_product_with_default_code.Orderline', function (require) {
    "use strict";
    var models = require('point_of_sale.models');
    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function () {
            var object_to_print = _super_orderline.export_for_printing.call(this);
            object_to_print.product_default_code = this.get_product().default_code
            console.log("YEEEEEEEEEEEEEEEEEEEEEEEEEES WE HAVE DO IT");
            console.log(object_to_print);
            return object_to_print;
        }
    });
})