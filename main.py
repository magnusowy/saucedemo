import torch
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model.pt')
results = model('some_image.jpg')
results.print()  # wykryte klasy