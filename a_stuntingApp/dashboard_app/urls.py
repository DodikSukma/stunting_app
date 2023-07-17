from django.urls import path
from . import views


urlpatterns = [
    #========================= HOME DASHBOARD PAGE ==========================
    path('',views.Admin, name='admin-page'),

    #========================= Agenda Page ==========================
    path('tambah_agenda/',views.Tambah_Agenda, name='tambah-agenda-page'),
    path('delete_agenda/<str:pk>/',views.Delete_Agenda, name='admin-page'),

    #========================= DATABASE PAGE ==========================
    path('menu_database/',views.menu_database, name='database-page-menu'),
    

    #========================= DATABASE PAGE BR 1 ==========================
    path('database_br_1/',views.database_br_1, name='database-page-br-1'),

    path('database_add_br_1/',views.AddDatabase_br_1, name='database-add-br-1'),
    
    path('database_br_1/database_delete_br_1/<int:pk>',views.DeleteDatabase_br_1, name='database-delete-br-1'),

    path('database_edit_br_1/<str:pk>/',views.EditDatabase_br_1, name='database-edit-br-1'),


    #========================= DATABASE PAGE BR 2 ==========================
    path('database_br_2/',views.database_br_2, name='database-page-br-2'),

    path('database_add_br_2/',views.AddDatabase_br_2, name='database-add-br-2'),
    
    path('database_br_2/database_delete_br_2/<int:pk>',views.DeleteDatabase_br_2, name='database-delete-br-2'),

    path('database_edit_br_2/<str:pk>/',views.EditDatabase_br_2, name='database-edit-br-2'),



    #========================= DATABASE PAGE ==========================
    path('menu_prediksi/',views.menu_prediksi, name='prediksi-page-menu'),

    #========================= PREDIKSI PAGE ==========================
    path('prediksi_stunting/',views.Prediksi, name='prediksi-page-library'),
    path('prediksi_stunting_develop/',views.prediksi_stunting_develop, name='prediksi-page-develop'),


    #======================== PREDIKSI PAGE DENGAN REKAPAN ====================
    path('rekapan_prediksi_stunting/',views.Prediksi_data_hasil, name='rekapan-prediksi-page'),

    path('rekap_prediksi/',views.rekap_prediksi, name='rekap_prediksi'),
    
    path('rekapan_prediksi_stunting/stunting_delete_rekap/<int:pk>',views.DeleteDatarekap, name='rekap-delete-stuning'),



    #========================= LOGIN REGISTER PAGE ==========================
    path('login_app/',views.loginPage, name='login-page'),

    path('register_app/',views.registerPage, name='register-page'),

    #========================= STUNTING INFO PAGE ==========================
    path('stunting_info/',views.StuntingInfo, name='stunting-info'),

    #========================= STUNTING INFO PAGE ==========================
    path('stunting_info_develop/',views.StuntingInfoDevelop, name='stunting-info-develop'),

    #========================= DATABASE DATA TRAINING ==========================
    path('data_training/',views.data_training, name='data-training-page'),

    path('data_training_add/',views.add_data_training, name='data-training-add-page'),
    
    path('data_training/data_training_delete/<int:pk>',views.DeleteDataTraining, name='data-training-delete-page'),

    path('data_training_update/<str:pk>/',views.EditDataTraining, name='data-training-edit-page'),

    #========================= DATABASE DATA TESTING ==========================
    path('data_testing/',views.data_testing, name='data-testing-page'),

    path('data_testing_add/',views.add_data_testing, name='data-testing-add-page'),
    
    path('data_testing/data_testing_delete/<int:pk>',views.DeleteDataTesting, name='data-testing-delete-page'),

    path('data_testing_update/<str:pk>/',views.EditDataTesting, name='data-testing-edit-page'),

    #========================= STUNTING INFO PAGE ==========================
    

]   