frappe.ui.form.on('Customer', {
    setup: function(frm) {
        frm.set_query("custom_default_receiving_warehouse", function() {
            return {
                filters: {
                    "company": frm.doc.represents_company,
                    "is_group": 0
                }
            };
        });

        frm.set_query("custom_default_buying_price_list", function() {
            return {
                filters: {
                    "buying": 1
                }
            };
        });

        frm.set_query("receiving_warehouse", "custom_receiving_branches", function(doc) {
            return {
                filters: {
                    "company": doc.represents_company,
                    "is_group": 0
                }
            };
        });

        frm.set_query("buying_price_list", "custom_receiving_branches", function() {
            return {
                filters: {
                    "buying": 1
                }
            };
        });
    }
});
