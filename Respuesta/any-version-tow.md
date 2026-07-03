I will start by listing the contents of the workspace directory to understand the structure of the project and find the existing draft.

Listed directory rescalafonamiento

I will list the contents of the `Respuesta` folder, which is where the current document is open.

Listed directory Respuesta

I will list the contents of the `Solicitud` folder, which contains the PDF document referenced by the user.

Listed directory Solicitud

I will view the file `analisis_respuesta_y_recurso.md` to examine the current analysis and the draft of the administrative appeal.

Viewed analisis_respuesta_y_recurso.md:1-122

I will view `read_pdfs.py` to see if there is already a script to read PDF files in the workspace.

Viewed read_pdfs.py:1-35

I will create a temporary Python script in the scratch folder to extract the text from the PDF document `SOLICITUD DE CAMBIO DE ESCALAFÓN Y ESPECIALIDAD.pdf` so we can inspect its contents.

Edited extract_solicitud.py

I will run the script to extract the content of the PDF.

Ran command: `.venv\Scripts\python C:\Users\31098540\.gemini\antigravity-ide\brain\7bd001b6-bfd0-4f6e-967c-3c01f44c2317\scratch\extract_solicitud.py`

I will run the Python script using the proper PowerShell syntax (`&` prefix for the script path).

Ran command: `& .venv\Scripts\python C:\Users\31098540\.gemini\antigravity-ide\brain\7bd001b6-bfd0-4f6e-967c-3c01f44c2317\scratch\extract_solicitud.py`

I will run the command using the absolute path to the virtual environment's Python executable.

Ran command: `& "g:\GNA-DOC\GNA-2026\rescalafonamiento\.venv\Scripts\python.exe" "C:\Users\31098540\.gemini\antigravity-ide\brain\7bd001b6-bfd0-4f6e-967c-3c01f44c2317\scratch\extract_solicitud.py"`

I will check if Python is available globally in the system command line.

Ran command: `python --version`

I will check if the `pypdf` library is installed in the global Python environment.

Ran command: `python -c "import pypdf; print(pypdf.__version__)"`

I will run the extraction script with the global Python executable.

Ran command: `python C:\Users\31098540\.gemini\antigravity-ide\brain\7bd001b6-bfd0-4f6e-967c-3c01f44c2317\scratch\extract_solicitud.py`

I will update the scratch Python script to write the extracted text to a text file in the scratch directory with UTF-8 encoding. This will prevent console encoding errors.

Edited extract_solicitud.py

I will run the updated PDF extraction script.

Ran command: `python C:\Users\31098540\.gemini\antigravity-ide\brain\7bd001b6-bfd0-4f6e-967c-3c01f44c2317\scratch\extract_solicitud.py`

I will read the extracted text from `solicitud_texto.txt`.

Viewed solicitud_texto.txt:1-800

I will read the rest of the extracted text from `solicitud_texto.txt` to capture the complete arguments.

Viewed solicitud_texto.txt:801-1329

I will view `solicitud_reescalafonamiento_vfinal.md` to see the structure of previous requests and how they address the chain of command.

Viewed solicitud_reescalafonamiento_vfinal.md:1-32

I will view `Respuesta\If_reescalafonamiento020726.txt` to read the exact wording of the rejection. This will allow us to tailor V2 of the appeal to address the specific arguments raised by the administration.

Viewed If_reescalafonamiento020726.txt:1-59

I will perform a search across the workspace for references to "vía jerárquica" or "vía" to see if there are standard formatting practices for elevations in the repository.

Searched for "jerárquica"

I will list the contents of the `Normativa GNA` directory to see if there is any regulation on petitions and resources (such as REP-30-01 or RV-30-01) that governs the format and submission of resources.

Listed directory Normativa%20GNA

I will search for the word "conducto" in `REP-30-01_inspected.txt` to see Gendarmería's regulations on how petitions and resources must be routed through the chain of command.

Searched for "conducto"

I will search for "jerárquic" (case-insensitive) in the regulations text file to find the specific procedure for presenting appeals through the hierarchical chain.

Searched for "jerárquic"

I will search for "jerarqu" (without the accent) in `REP-30-01_inspected.txt` to find references to the hierarchical channel.

Searched for "jerarqu"

I will search for the term "recurso" in `REP-30-01_inspected.txt` to find regulations on how administrative resources are defined and submitted.

Searched for "recurso"

I will view the first 100 lines of `REP-30-01_inspected.txt` to check its contents and structure.

Viewed REP-30-01_inspected.txt:1-100

I will view `analisis_reclamo_derechos.md` to see if there are other arguments or legal citations that we can use to strengthen our V2 appeal.

Viewed analisis_reclamo_derechos.md:1-50

I will create the new document `recurso_reescalafonamiento_v2.md` in the `Respuesta` directory. It will include:
1. **Nota de Elevación por Vía Jerárquica:** Addressed to the Chief of your Element (**Comandante Mayor D. Sergio José BESSONE**), requesting the elevation of your appeal.
2. **Recurso de Reconsideración y Jerárquico en Subsidio:** Addressed to the **Director de Recursos Humanos**, incorporating your complete academic timeline (as detailed in your `SOLICITUD`), and systematically refuting the points of the rejection (`IF-2026-60306296-APN-DIREMAN#GNA`).

Let's write this file.

I will write the file `recurso_reescalafonamiento_v2.md` directly into the workspace folder without the artifact metadata, as this is a project file.

Edited recurso_reescalafonamiento_v2.md

He creado un nuevo archivo con la versión 2 de tu escrito recursivo: [recurso_reescalafonamiento_v2.md](file:///g:/GNA-DOC/GNA-2026/rescalafonamiento/Respuesta/recurso_reescalafonamiento_v2.md).

Para cumplir con tu requerimiento de seguir la **cadena de comando (conducto reglamentario)** y basarnos exactamente en los hechos de tu [SOLICITUD DE CAMBIO DE ESCALAFÓN Y ESPECIALIDAD.pdf](file:///g:/GNA-DOC/GNA-2026/rescalafonamiento/Solicitud/SOLICITUD DE CAMBIO DE ESCALAFÓN Y ESPECIALIDAD.pdf), estructuré el documento en dos partes:

1. **Nota de Elevación por Vía Jerárquica:** Dirigida al Jefe de tu elemento actual, el **Comandante Mayor D. Sergio José BESSONE** (Jefe del Centro Asistencial "BUENOS AIRES"). Esta nota formaliza la solicitud de elevación de tu recurso a través del canal jerárquico reglamentario.
2. **Escrito del Recurso de Reconsideración y Jerárquico en Subsidio:** Dirigido al **Director de Recursos Humanos de la Fuerza**, pero presentado a través del conducto jerárquico. En este escrito:
   * **Se integró por completo tu historial académico y profesional** desde tu ingreso en 2009 (Subalférez "en comisión" y confirmación definitiva por `RESOLMS 1470`), detallando tus cursos en ciberseguridad, SQL Server, GIS, y tu participación técnica en sistemas de salud (certificaciones periódicas en el Hospital Italiano hasta 2025).
   * **Se resalta tu titulación de grado universitario:** La obtención de tu título de **Licenciado en Informática (UBP, 2014)** como el pilar fundamental que acredita tu idoneidad técnica actual.
   * **Se rebaten de forma categórica los puntos de la denegatoria (`IF-2026-60306296-APN-DIREMAN#GNA`):**
     * *Argumento de DIREMAN sobre título terciario de ingreso:* Demostramos que la Disposición `DI-2025-1198-APN-DINALGEN#GNA` (Art. 2) exige únicamente **revistar** en Reclutamiento Local ostentando título universitario habilitante en presente, por lo que exigir que este título sea el de ingreso es un exceso restrictivo que viola el principio de jerarquía de normas.
     * *Argumento sobre la especialidad no contemplada:* Explicamos que el reescalafonamiento se solicita hacia la Especialidad TIC de Apoyo Técnico sobre la base de tu Licenciatura en Informática (que sí encuadra), y que además la propia DIRTICOM propuso formalmente incluir la especialidad "Analista de Sistemas" (ASI) en el listado de aptitudes TIC (mediante `IF-2025-06897873`).
     * *Argumento de "igualdad ante la ley":* Refutamos la postura de DIREMAN aclarando que la verdadera igualdad (Art. 16 CN) consiste en tratar igual a quienes poseen idéntica idoneidad profesional en el presente, resultando discriminatorio ignorar un título de grado universitario de 2014.
     * *Falta de subplanes:* Sostenemos que la inacción de DIREMAN para crear los planes de transición (obligación impuesta por el Art. 3 de la DI-2025-1198) no puede ser utilizada por la administración como justificación para extinguir tu derecho.

Puedes revisar y editar el documento completo aquí: [recurso_reescalafonamiento_v2.md](file:///g:/GNA-DOC/GNA-2026/rescalafonamiento/Respuesta/recurso_reescalafonamiento_v2.md).