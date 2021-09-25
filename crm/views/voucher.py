from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from crm.models import Voucher
from crm.forms import VouchersForm
import csv

@login_required(login_url='login')
def voucher_list(request):
    vouchers = Voucher.objects.all()
    return render(request, 'voucher/voucher_list.html',
                  {'vouchers': vouchers})


@login_required(login_url='login')
def download_voucher_list(request):
    vouchers = Voucher.objects.all()
    with open("reports/voucher_report.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(vouchers)
    return render(request, 'voucher/voucher_list.html',
                  {'vouchers': vouchers})


@login_required(login_url='login')
def voucher_sorted_list(request):
    vouchers = Voucher.objects.order_by('count_of_days')
    return render(request, 'voucher/voucher_list.html',
                  {'vouchers': vouchers})


@login_required(login_url='login')
def voucher_details(request, pk):
    voucher = get_object_or_404(Voucher, pk=pk)
    return render(request, 'voucher/voucher_details.html',
                  {'voucher': voucher})


@permission_required('user.is_superuser', login_url='login')
def voucher_new(request):
    if request.method == "POST":
        form = VouchersForm(request.POST)
        if form.is_valid():
            voucher = form.save(commit=False)
            voucher.save()
            return redirect('voucher_details', pk=voucher.pk)
    else:
        form = VouchersForm()
    return render(request, 'voucher/voucher_add.html', {'form': form})


@permission_required('user.is_superuser', login_url='login')
def voucher_edit(request, pk):
    voucher = get_object_or_404(Voucher, pk=pk)
    if request.method == "POST":
        form = VouchersForm(request.POST, instance=voucher)
        if form.is_valid():
            voucher = form.save(commit=False)
            voucher.save()
            return redirect('voucher_details', pk=voucher.pk)
    else:
        form = VouchersForm(instance=voucher)
    return render(request, 'voucher/voucher_edit.html', {'form': form})


@permission_required('user.is_superuser', login_url='login')
def voucher_delete(request, pk):
    Voucher.objects.filter(pk=pk).delete()
    return voucher_list(request)
