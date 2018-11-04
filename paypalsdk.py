import paypalrestsdk
from paypalrestsdk import Payment
import logging
import requests

paypalrestsdk.configure({
  'mode': 'sandbox', #sandbox or live
  'client_id': 'AQXGfEbC_RWq6_scEvkYllGCmCJ2jjRVyInoFfGo-JKuZ5FuSU6ekb3T8Ix_mpmudPF-3zU9OrABbMsx',
  'client_secret': 'EEVc-WFduPeFU_fKOuuGFEfO3-3l5gS963TOY5-myXYWIZ5wWvcAlentcrSkcTpZxyV1grQJtcK8zsPN',
})

payment=[]

payment1 = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item1",
                "sku": "item",
                "price": "9.42",
                "currency": "USD",
                "quantity": 2}]},
        "amount": {
            "total": "18.84",
            "currency": "USD"},
        "payee":{"merchant_id":"123451009"},
        "description":"This is the payments transaction description."}]})

        #-------------------------------------------------------------------
payment2 = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item2",
                "sku": "item",
                "price": "33.5",
                "currency": "USD",
                "quantity": 1}]},
        "amount": {
            "total": "33.5",
            "currency": "USD"},
        "payee":{"merchant_id" : "123452200"},
        "description":"This is the payments transaction description."}]})

    #-------------------------------------------------------------------
payment3 = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item3",
                "sku": "item",
                "price": "100",
                "currency": "USD",
                "quantity": 2}]},
        "amount": {
            "total": "100",
            "currency": "USD"},
        "payee":{"merchant_id":"123452227"},
        "description":"This is the payment transaction description."}]});
    #-------------------------------------------------------------------
payment4 = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item4",
                "sku": "item",
                "price": "4.56",
                "currency": "USD",
                "quantity": 1}]},
        "amount": {
            "total": "4.56",
            "currency": "USD"},
        "payee":{"merchant_id":"123451017"},
        "description":"This is the payment transaction description."}]});

arrayPay=[payment1['transactions'][0]['payee']["merchant_id"],payment2['transactions'][0]['payee']["merchant_id"],payment3['transactions'][0]['payee']["merchant_id"],payment4['transactions'][0]['payee']["merchant_id"]]


arrayMoney=[payment1['transactions'][0]['amount']["total"],payment2['transactions'][0]['amount']["total"],payment3['transactions'][0]['amount']["total"],payment4['transactions'][0]['amount']["total"]]
