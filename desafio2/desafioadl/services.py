from desafioadl.models import Tarea, SubTarea

def recupera_tareas_y_subtareas():
    tareas = Tarea.objects.all() 
    todas_las_tareas = []
    for tarea in tareas:
        item = {
            'tarea': tarea,
            'sub_tareas': tarea.subtarea_set.filter(eliminada=False) 
        }
        todas_las_tareas.append(item)

    return todas_las_tareas

def crear_nueva_tarea():
    tarea = Tarea(descripcion="", eliminada=False)
    tarea.save()
    return recupera_tareas_y_subtareas()

def crear_sub_tarea(tarea_id, descripcion=""):
    # Se necesita el ID de la tarea padre para crear una sub_tarea
    tarea= Tarea.objects.get(id=tarea_id)  # Obtener el objeto de Tarea correspondiente
    sub_tarea = SubTarea(descripcion=descripcion, eliminada=False, tarea_id=tarea)
    sub_tarea.save()
    return recupera_tareas_y_subtareas()
    

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return recupera_tareas_y_subtareas()

def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.delete()
    return recupera_tareas_y_subtareas()

def imprimir_en_pantalla(arreglo):
    for tarea in arreglo:
        print(f"[{tarea['tarea'].id}] {tarea['tarea'].descripcion}")
        for subtarea in tarea['sub_tareas']:
            print(f"    [{subtarea.id}] {subtarea.descripcion}")