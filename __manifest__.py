# -*- coding: utf-8 -GPK*-

{
    'name': 'Hospital',
    'version': '1.0',
    'author': 'Yali Technologies',
    'category': 'Hostial ERP',
    'sequence': 1,
    'website': 'www.yalitechnologies.com',
    'depends': ['base', 'board', 'mail'],
    'data': [
        'menu/menu.xml',

        'views/common/patient.xml',
        'views/patient/opt_appointment.xml',
        'views/patient/opt.xml',
        'views/patient/ipt.xml',
        'views/patient/ambulance.xml',
        'views/patient/admission.xml',
        'views/patient/treatment.xml',
        'views/patient/doctor_visit.xml',
        'views/patient/remainder.xml',
        'views/patient/hospitality.xml',
        'views/patient/deceased.xml',
        'views/patient/medicine.xml',
        'menu/patient.xml',

        'views/common/employee.xml',
        'views/common/awards.xml',
        'views/common/course.xml',
        'views/common/experience.xml',
        'views/common/education.xml',
        'menu/employee.xml',

        'views/common/relation.xml',
        'views/common/employee_type.xml',
        'views/common/bank.xml',
        'views/common/blood_group.xml',
        'views/common/state.xml',
        'views/common/country.xml',
        'menu/hospital.xml',

    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
