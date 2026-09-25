frappe.ui.form.on('Sales Invoice', {
    customer: function(frm) {
        if (frm.doc.customer) {
            frappe.db.get_value('Customer', frm.doc.customer, ['is_internal_customer', 'custom_is_branch_wise_receiving']).then(r => {
                if (r.message && r.message.is_internal_customer && r.message.custom_is_branch_wise_receiving) {
                    frm.set_df_property('custom_receiving_branch', 'hidden', 0);
                    frm.set_df_property('custom_receiving_branch', 'reqd', 1);

                    // Fetch mapped branches and set query
                    frappe.call({
                        method: "frappe.client.get",
                        args: {
                            doctype: "Customer",
                            name: frm.doc.customer
                        },
                        callback: function(res) {
                            if (res.message && res.message.custom_receiving_branches) {
                                let branches = res.message.custom_receiving_branches.map(d => d.branch);
                                frm.set_query('custom_receiving_branch', function() {
                                    return {
                                        filters: {
                                            'name': ['in', branches]
                                        }
                                    };
                                });
                            }
                        }
                    });
                } else {
                    frm.set_df_property('custom_receiving_branch', 'hidden', 1);
                    frm.set_df_property('custom_receiving_branch', 'reqd', 0);
                    frm.set_value('custom_receiving_branch', '');
                }
            });
        } else {
            frm.set_df_property('custom_receiving_branch', 'hidden', 1);
            frm.set_df_property('custom_receiving_branch', 'reqd', 0);
            frm.set_value('custom_receiving_branch', '');
        }
    }
});
