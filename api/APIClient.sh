echo  "Número de publicações na conferência AAAI da área ai"
curl -i "http://localhost:5000/publications?areaName=ai&conferenceName=AAAI"
echo  "Número de publicações na conferência UAI da área ai"
curl -i "http://localhost:5000/publications?areaName=ai&conferenceName=UAI"
###############################################################################
echo  "Número de publicações no conjunto de conferências da área de se"
curl -i "http://localhost:5000/publications?areaName=se"
echo  "Número de publicações no conjunto de conferências da área de ai"
curl -i "http://localhost:5000/publications?areaName=ai"
###############################################################################
echo  "Scores de todos os departamentos da área ai"
curl -i "http://localhost:5000/scores?areaName=ai"
echo  "Scores de todos os departamentos da área se"
curl -i "http://localhost:5000/scores?areaName=se"
###############################################################################
echo  "Score do departamento UFRJ na área se"
curl -i "http://localhost:5000/scores?areaName=se&departmentName=UFRJ"
echo  "Score do departamento UFMG na área se"
curl -i "http://localhost:5000/scores?areaName=se&departmentName=UFMG"
###############################################################################
echo  "Número de professores que publicam na área ai"
curl -i "http://localhost:5000/teachers?areaName=ai"
echo  "Número de professores que publicam na área se"
curl -i "http://localhost:5000/teachers?areaName=se"
###############################################################################
echo  "Número de professores do departamento UFMG que publicam na área se"
curl -i "http://localhost:5000/teachers?areaName=se&departmentName=UFMG"
echo  "Número de professores do departamento UFRJ que publicam na área se"
curl -i "http://localhost:5000/teachers?areaName=se&departmentName=UFRJ"
###############################################################################
echo  "Lista de papers da área ai "
curl -i "http://localhost:5000/papers?areaName=ai"
echo  "Lista de papers da área se "
curl -i "http://localhost:5000/papers?areaName=se"
###############################################################################
echo  "Lista de papers da área se no ano 2017"
curl -i "http://localhost:5000/papers?areaName=se&year=2017"
echo  "Lista de papers da área se no ano 2016"
curl -i "http://localhost:5000/papers?areaName=se&year=2016"
###############################################################################
echo  "Lista de papers do departamento UFMG na área ai"
curl -i "http://localhost:5000/papers?areaName=ai&departmentName=UFMG"
echo  "Lista de papers do departamento UFRJ na área ai"
curl -i "http://localhost:5000/papers?areaName=ai&departmentName=UFRJ"
###############################################################################
echo  "Lista de papers do professor Rodrigo Barros"
curl -i "http://localhost:5000/papers?teacherName=Rodrigo-Barros"
echo  "Lista de papers do professor  Rodrigo Bonifacio"
curl -i "http://localhost:5000/papers?teacherName=Rodrigo-Bonifacio"