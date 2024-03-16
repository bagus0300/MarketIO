from django.shortcuts import render
from django.conf import settings as DJANGO_SETTINGS
from mailchimp_marketing.api_client import ApiClientError
import mailchimp_marketing as MailchimpMarketing
from django.http import HttpResponse
import json


def subscribe(request):
    """
    View function for subscribing to the newsletter.

    Response:
    HttpResponse with a message indicating the result of the subscription attempt.
    """
    mailchimp = MailchimpMarketing.Client()
    mailchimp.set_config(
        {
            "api_key": DJANGO_SETTINGS.MAILCHIMP_API_KEY,
            "server": DJANGO_SETTINGS.MAILCHIMP_DATA_CENTER,
        }
    )
    list_id = DJANGO_SETTINGS.MAILCHIMP_LIST_ID
    member_info = {"email_address": request.POST.get("email"), "status": "subscribed"}
    response = mailchimp.lists.get_list(list_id)
    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        return HttpResponse("Success! Keep an eye on your inbox for updates.")
    except ApiClientError as error:
        error_json = json.loads(error.text)
        if error_json.get("title") == "Member Exists":
            return HttpResponse("You are already subscribed.")
        return HttpResponse("An error occurred. Please try again later.")
