from odoo import models, fields, api,  _


class accrMedicalUnitMedicine(models.Model):

    _name = "accr.medical.unit.medicine"
    _description = "ACCR Medical Unit Medicines"

    name = fields.Char(string=u'Medicine', required=True)
    discription = fields.Text(string=u'Description')
    alternetive_medicines = fields.Many2many('accr.medical.unit.medicine', 'accr_medical_unit_medicines_rel',
                                               'medicine_1_id', 'medicine_2_id', string=u'Alternetive Medicines')
    side_effects = fields.Many2many('accr.medical.unit.medicine.side.effects',
                                    'accr_medical_unit_medicines_side_effects_rel', 'medicine_id', 'side_effects_id', string=u'Side Effects')

    drug_interaction = fields.Many2many('accr.medical.unit.medicine', 'accr_medical_unit_drug_interaction_rel',
                                               'drug_1_id', 'drug_2_id', string=u'Drug Interaction')              


    @api.onchange('alternetive_medicines')
    def _onchange_alternetive_medicines(self):
        for record in self:
            for alt_medicine in record.alternetive_medicines:
                medicine = self.env['accr.medical.unit.medicine'].search([('id','=',alt_medicine.id)])
                medicine.name = 'medice 22'
                medicine.alternetive_medicines.write(0,0, {'medicine_2_id': record.id})
            
    
    
                      

