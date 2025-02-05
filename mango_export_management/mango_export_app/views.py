from django.shortcuts import render, get_object_or_404, redirect
from .models import MangoExport
from .forms import MangoExportForm

def mango_list(request):
    query = request.GET.get('search', '')
    mangos = MangoExport.objects.all()

    if query:
        if query.isdigit():  # Check if input is an integer (order_id)
            mangos = mangos.filter(order_id=query)
        else:  # Otherwise, treat it as a variety (title)
            mangos = mangos.filter(variety__icontains=query)  # case-insensitive search

    return render(request, 'mango_export_app/mango_list.html', {'mangos': mangos, 'query': query})

def mango_create(request):
    if request.method == "POST":
        form = MangoExportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mango_list')
    else:
        form = MangoExportForm()
    return render(request, 'mango_export_app/mango_form.html', {'form': form})

# def mango_update(request, order_id):  # Change id -> order_id
#     mango = get_object_or_404(MangoExport, order_id=order_id)  # Change id -> order_id
#     if request.method == "POST":
#         form = MangoExportForm(request.POST, instance=mango)
#         if form.is_valid():
#             form.save()
#             return redirect('mango_list')
#     else:
#         form = MangoExportForm(instance=mango)
#     return render(request, 'mango_export_app/mango_form.html', {'form': form})
def mango_update(request, order_id):
    mango = get_object_or_404(MangoExport, order_id=order_id)
    if request.method == "POST":
        form = MangoExportForm(request.POST, instance=mango)
        if form.is_valid():
            form.save()
            return redirect('mango_list')
    else:
        form = MangoExportForm(instance=mango)
    return render(request, 'mango_export_app/mango_form.html', {'form': form})

def mango_delete(request, order_id):  # Change id -> order_id
    mango = get_object_or_404(MangoExport, order_id=order_id)  # Change id -> order_id
    if request.method == "POST":
        mango.delete()
        return redirect('mango_list')
    return render(request, 'mango_export_app/mango_confirm_delete.html', {'mango': mango})
