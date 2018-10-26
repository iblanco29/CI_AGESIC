from django.shortcuts import render

persons = [
	{
		'name': 'Ignacio',
		'surname1': 'Blanco',
		'surname2': 'Voeikoff',
		'idNumber': '4773067-6'
	}
]

def home(request):
	return render(request, 'face_verification/index.html')

def info(request):
	return render(request, 'face_verification/info.html')

def camera(request):
	return render(request, 'face_verification/camera.html')

def success(request):
	context = {
		'persons': persons
	}
	return render(request, 'face_verification/success.html', context)

def failure(request):
	return render(request, 'face_verification/failure.html')