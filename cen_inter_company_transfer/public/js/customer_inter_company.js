frappe.ui.form.on('Customer', {
    setup: function(frm) {
        let warehouse_query = function() {
            return {
                filters: {
                    "company": frm.doc.represents_company,
                    "is_group": 0
                }
            };
        };

        frm.set_query("custom_default_receiving_warehouse", warehouse_query);
        frm.set_query("receiving_warehouse", "custom_receiving_branches", warehouse_query);
    }
});
