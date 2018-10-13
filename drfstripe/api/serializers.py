from rest_framework import serializers
from .abstract import JSONSerializerField

ModelSerializer = serializers.ModelSerializer
Serializer = serializers.Serializer

from .. import settings as app_settings
from ..models import (
    EventProcessingException,
    Event,
    Transfer,
    TransferChargeFee,
    TransferChargeFee,
    Customer,
    CurrentSubscription,
    Invoice,
    InvoiceItem,
    Charge
)

"""
    Model API Serializers
"""


class EventProcessingExceptionSerializer(ModelSerializer):
    class Meta:
        model = EventProcessingException
        fields = '__all__'


class EventSerializer(ModelSerializer):
    event_processing_exceptions = EventProcessingExceptionSerializer(source='event_processing_exception_serializer_set', many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class CurrentSubscriptionSerializer(ModelSerializer):
    class Meta:
        model = CurrentSubscription
        fields = '__all__'


class ChargeSerializer(ModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'


class InvoiceItemSerializer(ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'


class InvoiceSerializer(ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)
    charges = ChargeSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class CurrentCustomerSerializer(ModelSerializer):
    has_active_subscription = serializers.ReadOnlyField()
    can_charge = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = '__all__'


"""
    Custom API Serializers
"""


class SubscriptionSerializer(Serializer):
    stripe_plan = serializers.ChoiceField(choices=app_settings.PLAN_CHOICES, required=True)


class CardSerializer(Serializer):
    number = serializers.IntegerField(help_text=u'The card number, as a string without any separators.', required=True)
    exp_month = serializers.IntegerField(help_text=u"Two digit number representing the card's expiration month.", required=True)
    exp_year = serializers.IntegerField(help_text=u"Two or four digit number representing the card's expiration year.", required=True)
    cvc = serializers.IntegerField(help_text=u'Card security code.', required=True)

    name = serializers.CharField(help_text=u"Cardholder's full name.", required=False, allow_null=True)
    address_line1 = serializers.CharField(required=False, allow_null=True)
    address_line2 = serializers.CharField(required=False, allow_null=True)
    address_city = serializers.CharField(required=False, allow_null=True)
    address_zip = serializers.CharField(required=False, allow_null=True)
    address_state = serializers.CharField(required=False, allow_null=True)
    address_country = serializers.CharField(required=False, allow_null=True)


class CardTokenSerializer(Serializer):
    token = serializers.CharField(required=True, help_text=u'Card token generated by stripe.js, or other api call.')


class CancelSerializer(Serializer):
    confirm = serializers.BooleanField(required=True)

    def validate_confirm(self, value):
        if value is False:
            raise serializers.ValidationError(u"Please confirm to continue.")
        return value


class WebhookSerializer(Serializer):
    data = JSONSerializerField(required=True, allow_null=False)