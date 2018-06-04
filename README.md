# info_view
Odoo Info view for Odoo

Usage:

```python
return {
    'name': 'Title',
    'type': 'ir.actions.act_window',
    'res_model': 'info_view.view',
    'view_mode': 'info',
    'view_type': 'info',
    'target': 'new',
    'context': {'message': 'This is the info message.'}
    }
```
