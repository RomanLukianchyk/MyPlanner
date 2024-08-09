from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from documents.models import Document
from documents.forms import DocumentForm


@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'documents/document_list.html', {'documents': documents})


@login_required
def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    return render(request, 'documents/document_detail.html', {'document': document})


@login_required
def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/document_form.html', {'form': form})


@login_required
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    if request.method == 'POST':
        document.file_path.delete()
        document.delete()
        return redirect('document_list')
    return render(request, 'documents/document_confirm_delete.html', {'document': document})
