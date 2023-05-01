from .models import Pelicula, Serie
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@login_required
@require_GET
def obtener_aleatoria(request, tipo):
    if tipo == 'pelicula':
        objeto = Pelicula.objects.order_by('?').first()
    elif tipo == 'serie':
        objeto = Serie.objects.order_by('?').first()
    else:
        return JsonResponse({'error': 'Tipo de objeto no válido'})
    
    data = {
        'nombre': objeto.nombre,
        'tipo': tipo,
        'genero': objeto.genero,
        'puntaje': objeto.puntaje,
    }
    return JsonResponse(data)
@login_required
@require_GET
def obtener_todas(request, tipo, orden):
    if tipo == 'pelicula':
        objetos = Pelicula.objects.all()
    elif tipo == 'serie':
        objetos = Serie.objects.all()
    else:
        return JsonResponse({'error': 'Tipo de objeto no válido'})
    
    if orden == 'nombre':
        objetos = objetos.order_by('nombre')
    elif orden == 'tipo':
        objetos = objetos.order_by('tipo')
    elif orden == 'genero':
        objetos = objetos.order_by('genero')
    elif orden == 'puntaje':
        objetos = objetos.order_by('-puntaje')
    else:
        return JsonResponse({'error': 'Orden no válido'})
    
    data = [{
        'nombre': obj.nombre,
        'tipo': tipo,
        'genero': obj.genero,
        'puntaje': obj.puntaje,
    } for obj in objetos]
    return JsonResponse(data, safe=False)

@login_required
@require_GET
def filtrar(request, tipo):
    if tipo == 'pelicula':
        objetos = Pelicula.objects.all()
    elif tipo == 'serie':
        objetos = Serie.objects.all()
    else:
        return JsonResponse({'error': 'Tipo de objeto no válido'})
    
    nombre = request.GET.get('nombre')
    genero = request.GET.get('genero')
    
    if nombre:
        objetos = objetos.filter(nombre__icontains=nombre)
    
    if genero:
        objetos = objetos.filter(genero=genero)
    
    data = [{
        'nombre': obj.nombre,
        'tipo': tipo,
        'genero': obj.genero,
        'puntaje': obj.puntaje,
    } for obj in objetos]
    return JsonResponse(data, safe=False)

@login_required
@require_POST
def marcar_vista(request, tipo, id):
    if tipo == 'pelicula':
        objeto = Pelicula.objects.get(id=id)
    elif tipo == 'serie':
        objeto = Serie.objects.get(id=id)
    else:
        return JsonResponse({'error': 'Tipo de objeto no válido'})
    
    vistas_anteriores = objeto.visualizaciones
    objeto.visualizaciones += 1
    objeto.save()
    
    vistas_actuales = objeto.visualizaciones
    
    data = {
        'mensaje': f'{objeto.nombre} marcada como vista',
        'vistas_anteriores': vistas_anteriores,
        'vistas_actuales': vistas_actuales
    }
    return JsonResponse(data)
@login_required
@require_POST
def puntuar(request, tipo, id, puntuacion=None):
    if tipo == 'pelicula':
        objeto = Pelicula.objects.get(pk=id)
    elif tipo == 'serie':
        objeto = Serie.objects.get(pk=id)
    else:
        return JsonResponse({'error': 'Tipo de objeto no válido'})
    
    puntaje = float(puntuacion)
    if not (1 <= puntaje <= 5):
        return JsonResponse({'error': 'Puntaje no válido'})
    
    puntaje_anterior = objeto.puntaje
        
    objeto.suma_puntajes += puntuacion
    objeto.cantidad_puntuaciones += 1
    objeto.puntaje = objeto.suma_puntajes / objeto.cantidad_puntuaciones
    objeto.save()
    
    mensaje = f'El puntaje anterior era {puntaje_anterior:.2f}. '
    mensaje += f'El nuevo puntaje es {objeto.puntaje:.2f}.'
    
    return JsonResponse({'mensaje': mensaje})





    

