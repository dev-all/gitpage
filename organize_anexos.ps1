$src = "g:\GNA-DOC\GNA-2026\rescalafonamiento\Normativa GNA\TitulosAcademicos"
$dst = "g:\GNA-DOC\GNA-2026\rescalafonamiento\Anexos_Presentacion"

if (-not (Test-Path $dst)) {
    New-Item -ItemType Directory -Force -Path $dst | Out-Null
}

Write-Host "Copiando y renombrando Anexo 01 (Analista Programador)..."
Copy-Item -Path "$src\analista programador\analista programador frente.png" -Destination "$dst\Anexo_01A_Titulo_Analista_Programador_Frente.png" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\analista programador\analista programador dorso.png" -Destination "$dst\Anexo_01B_Titulo_Analista_Programador_Dorso.png" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\analista programador\analista programador trayectoria.jpg" -Destination "$dst\Anexo_01C_Analitico_Analista_Programador.jpg" -ErrorAction SilentlyContinue

Write-Host "Copiando y renombrando Anexos 02 al 05 (Formación Inicial)..."
Copy-Item -Path "$src\congreso de comunicaciones e informatica 2010.pdf" -Destination "$dst\Anexo_02_Congreso_Comunicaciones_2010.pdf" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\Programacion web IAC.pdf" -Destination "$dst\Anexo_03_Programacion_Web_IAC.pdf" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\Diseo e implementacion SQL Server 2012.pdf" -Destination "$dst\Anexo_04_Diseno_Implementacion_SQL_Server_2012.pdf" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\Administracion SQL Server.pdf" -Destination "$dst\Anexo_05_Administracion_SQL_Server.pdf" -ErrorAction SilentlyContinue

Write-Host "Copiando y renombrando Anexos 06 al 07 (Ciberseguridad UTN)..."
Copy-Item -Path "$src\Certificados SGSI.pdf" -Destination "$dst\Anexo_06_Curso_SGSI_ISO27001_UTN_2017.pdf" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\Ciberseguridad UTN.pdf" -Destination "$dst\Anexo_07_Especializacion_Ciberseguridad_UTN.pdf" -ErrorAction SilentlyContinue

Write-Host "Copiando y renombrando Anexos 08 al 10 (Formación Complementaria)..."
Copy-Item -Path "$src\centro aeroterra\centro capacitacion aeroterra.pdf" -Destination "$dst\Anexo_08_GIS_Centro_Aeroterra.pdf" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\congreso odontologico 2019.pdf" -Destination "$dst\Anexo_09_Congreso_Odontologico_2019.pdf" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\Hospital Italiano\ServletSalidaCodificada.pdf" -Destination "$dst\Anexo_10A_Sistemas_Hospital_Italiano_1.pdf" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\Hospital Italiano\2023ServletSalidaCodificada.pdf" -Destination "$dst\Anexo_10B_Sistemas_Hospital_Italiano_2.pdf" -ErrorAction SilentlyContinue

Write-Host "Copiando y renombrando Anexo 11 (Título Grado UBP)..."
Copy-Item -Path "$src\lic inf ubp\lic inf 1.png" -Destination "$dst\Anexo_11A_Titulo_Licenciatura_Informatica_UBP_Frente.png" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\lic inf ubp\lic inf.png" -Destination "$dst\Anexo_11B_Titulo_Licenciatura_Informatica_UBP_Dorso.png" -ErrorAction SilentlyContinue
Copy-Item -Path "$src\lic inf ubp\lic inf.jpg" -Destination "$dst\Anexo_11C_Analitico_Licenciatura_Informatica_UBP.jpg" -ErrorAction SilentlyContinue

Write-Host "¡Proceso de renombrado finalizado! Los archivos están en la carpeta Anexos_Presentacion."
