from django.db import models
from django.contrib.auth.models import User

RC = 'Representante de Casilla' 
RG = 'Representante General'
MV = 'Movilizador'
SP = 'Simpatizante'

puesto_status = [
    (RC, 'Representante de Casilla'),
    (RG, 'Representante General'),
    (MV, 'Movilizador'),
    (SP, 'Simpatizante')
    ]


VA='Vasti Arana'
IBP='Isrrael y Profe'
OC='Omar Castellanos'
EC='Esther Castellanos'
CE='Cesar'
BE='Bere'
CL='Caleb Lupian'
ALO='Alonso'
AL='Abner Lopez'
ED='Edgar'
IS='Isai'
DP='Don Peter'
AD='Adin'


coordinador_status = [
    (VA, 'Vasti Arana'),
    (IBP, 'Israel y Profe'),
    (OC, 'Omar Castellanos'),
    (EC, 'Esther Castellanos'),
    (CE, 'Cesar'),
    (BE, 'Bere'),
    (CL, 'Caleb Lupian'),
    (ALO, 'Alonso'),
    (AL, 'Abner Lopez'),
    (ED, 'Edgar'),
    (IS, 'Isai'),
    (DP, 'Don Peter'),
    (AD, 'Adin')
    ]


GDL='Guadalajara'


municipio_status = [
    (GDL, 'Guadalajara')
    ]

JAL='Jalisco'

estado_status = [
    (JAL, 'Jalisco')
    ]

seccion_status = [
    (633, '0633'),
    (634, '0634'),
    (635, '0635'),
    (636, '0636'),
    (637, '0637'),
    (638, '0638'),
    (639, '0639'),
    (640, '0640'),
    (641, '0641'),
    (642, '0642'),
    (643, '0643'),
    (644, '0644'),
    (645, '0645'),
    (646, '0646'),
    (647, '0647'),
    (648, '0648'),
    (649, '0649'),
    (650, '0650'),
    (651, '0651'),
    (652, '0652'),
    (653, '0653'),
    (654, '0654'),
    (655, '0655'),
    (656, '0656'),
    (657, '0657'),
    (658, '0658'),
    (659, '0659'),
    (660, '0660'),
    (661, '0661'),
    (662, '0662'),
    (663, '0663'),
    (664, '0664'),
    (708, '0708'),
    (709, '0709'),
    (710, '0710'),
    (711, '0711'),
    (712, '0712'),
    (713, '0713'),
    (714, '0714'),
    (715, '0715'),
    (716, '0716'),
    (717, '0717'),
    (718, '0718'),
    (719, '0719'),
    (720, '0720'),
    (1187, '1187'),
    (1188, '1188'),
    (1189, '1189'),
    (1190, '1190'),
    (1191, '1191'),
    (1192, '1192'),
    (1193, '1193'),
    (1194, '1194'),
    (1195, '1195'),
    (1196, '1196'),
    (1197, '1197'),
    (1198, '1198'),
    (1199, '1199'),
    (1200, '1200'),
    (1201, '1201'),
    (1202, '1202'),
    (1203, '1203'),
    (1204, '1204'),
    (1205, '1205'),
    (1206, '1206'),
    (1207, '1207'),
    (1208, '1208'),
    (1209, '1209'),
    (1210, '1210'),
    (1211, '1211'),
    (1212, '1212'),
    (1213, '1213'),
    (1214, '1214'),
    (1215, '1215'),
    (1216, '1216'),
    (1217, '1217'),
    (1218, '1218'),
    (1219, '1219'),
    (1220, '1220'),
    (1221, '1221'),
    (1222, '1222'),
    (1223, '1223'),
    (1224, '1224'),
    (1225, '1225'),
    (1226, '1226'),
    (1227, '1227'),
    (1228, '1228'),
    (1229, '1229'),
    (1230, '1230'),
    (1231, '1231'),
    (1232, '1232'),
    (1233, '1233'),
    (1234, '1234'),
    (1235, '1235'),
    (1236, '1236'),
    (1237, '1237'),
    (1238, '1238'),
    (1239, '1239'),
    (1240, '1240'),
    (1241, '1241'),
    (1242, '1242'),
    (1243, '1243'),
    (1244, '1244'),
    (1245, '1245'),
    (1246, '1246'),
    (1247, '1247'),
    (1248, '1248'),
    (1249, '1249'),
    (1250, '1250'),
    (1251, '1251'),
    (1252, '1252'),
    (1253, '1253'),
    (1254, '1254'),
    (1255, '1255'),
    (1256, '1256'),
    (1257, '1257'),
    (1258, '1258'),
    (1259, '1259'),
    (1260, '1260'),
    (1261, '1261'),
    (1262, '1262'),
    (1263, '1263'),
    (1264, '1264'),
    (1265, '1265'),
    (1266, '1266'),
    (1267, '1267'),
    (1268, '1268'),
    (1269, '1269'),
    (1270, '1270'),
    (1271, '1271'),
    (1272, '1272'),
    (1273, '1273'),
    (1274, '1274'),
    (1275, '1275'),
    (1276, '1276'),
    (1277, '1277'),
    (1278, '1278'),
    (1279, '1279'),
    (1280, '1280'),
    (1281, '1281'),
    (1282, '1282'),
    (1283, '1283'),
    (1284, '1284'),
    (1285, '1285'),
    (1286, '1286'),
    (1287, '1287'),
    (1288, '1288'),
    (1289, '1289'),
    (1290, '1290'),
    (1291, '1291'),
    (1292, '1292'),
    (1293, '1293'),
    (1294, '1294'),
    (1295, '1295'),
    (1296, '1296'),
    (1297, '1297'),
    (1298, '1298'),
    (1299, '1299'),
    (1300, '1300'),
    (1301, '1301'),
    (1302, '1302'),
    (1303, '1303'),
    (1304, '1304'),
    (1305, '1305'),
    (1306, '1306'),
    (1307, '1307'),
    (1308, '1308'),
    (1309, '1309'),
    (1310, '1310'),
    (1311, '1311'),
    (1312, '1312'),
    (1313, '1313'),
    (1314, '1314'),
    (1315, '1315'),
    (1316, '1316'),
    (1317, '1317'),
    (1318, '1318'),
    (1319, '1319'),
    (1320, '1320'),
    (1321, '1321'),
    (1322, '1322'),
    (1323, '1323'),
    (1324, '1324'),
    (1325, '1325'),
    (1326, '1326'),
    (1327, '1327'),
    (1328, '1328'),
    (1329, '1329'),
    (1330, '1330'),
    (1331, '1331'),
    (1332, '1332'),
    (1333, '1333'),
    (1334, '1334'),
    (1335, '1335'),
    (1336, '1336'),
    (1337, '1337'),
    (1338, '1338'),
    (1339, '1339'),
    (1340, '1340'),
    (1341, '1341'),
    (1342, '1342'),
    (1343, '1343'),
    (1344, '1344'),
    (1345, '1345'),
    (1346, '1346'),
    (1347, '1347'),
    (1348, '1348'),
    (1349, '1349'),
    (1350, '1350'),
    (1351, '1351'),
    (1352, '1352'),
    (1353, '1353'),
    (1354, '1354'),
    (1355, '1355'),
    (1356, '1356'),
    (1357, '1357'),
    (1358, '1358'),
    (1359, '1359'),
    (1360, '1360'),
    (1361, '1361'),
    (1362, '1362'),
    (1363, '1363'),
    (1364, '1364'),
    (1365, '1365'),
    (1366, '1366'),
    (1367, '1367'),
    (1368, '1368'),
    (1369, '1369'),
    (1370, '1370'),
    (1371, '1371'),
    (1372, '1372'),
    (1373, '1373'),
    (3716, '3716'),
    (3717, '3717'),
    (3718, '3718'),
    (3719, '3719'),
    (3720, '3720')
    ]

age = [
    (18, '18'),
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
    (26, '26'),
    (27, '27'),
    (28, '28'),
    (29, '29'),
    (30, '30'),
    (31, '31'),
    (32, '32'),
    (33, '33'),
    (34, '34'),
    (35, '35'),
    (36, '36'),
    (37, '37'),
    (38, '38'),
    (39, '39'),
    (40, '40'),
    (41, '41'),
    (42, '42'),
    (43, '43'),
    (44, '44'),
    (45, '45'),
    (46, '46'),
    (47, '47'),
    (48, '48'),
    (49, '49'),
    (50, '50'),
    (51, '51'),
    (52, '52'),
    (53, '53'),
    (54, '54'),
    (55, '55'),
    (56, '56'),
    (57, '57'),
    (58, '58'),
    (59, '59'),
    (60, '60'),
    (61, '61'),
    (62, '62'),
    (63, '63'),
    (64, '64'),
    (65, '65'),
    (66, '66'),
    (67, '67'),
    (68, '68'),
    (69, '69'),
    (70, '70'),
    (71, '71'),
    (72, '72'),
    (73, '73'),
    (74, '74'),
    (75, '75')
    ]

# Create your models here.
class Task(models.Model):
    participacion = models.CharField(max_length=100, null=False, blank=False, choices=puesto_status)
    nombre_completo = models.CharField(max_length=150)
    edad = models.IntegerField(null= False, blank=False, choices=age, default=age, help_text = 'Selecciona tu Edad')
    calle_y_numero = models.CharField(max_length=250)
    masculino = models.BooleanField(default=False)
    femenino = models.BooleanField(default=False)
    colonia = models.CharField(max_length=200)
    c_p = models.CharField('C.P', max_length=250)
    municipio = models.CharField(max_length=250, null=False, blank=False, choices=municipio_status, default=None)
    estado = models.CharField(max_length=250, null=False, blank=False, choices=estado_status, default= None)
    num_seccion = models.IntegerField('Nº de Seccion', null=False, blank=False, choices=seccion_status, help_text='Selecciona una Seccion' )   
    num_casilla = models.CharField('Nº de Casilla',max_length=250, blank=True, help_text='Ingresa Num de Casilla',)
    nombre_enlace = models.CharField(max_length=250, null=False, blank=False, choices=coordinador_status, help_text='Selecciona tu Coordinador',)
    description = models.TextField('Comentarios',blank=True, default= 'Ingrese sus Comentarios (Opcional)')
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField('Fecha',null=True, help_text='Ejemplo: yyyy-mm-dd')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.participacion + self.nombre_completo + ' - by ' + self.user.username