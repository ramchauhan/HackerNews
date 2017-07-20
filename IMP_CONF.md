# override the mandatory fields Expception
# Example

class TestAppSerializer(serializers.ModelSerializer):
    """
    Model Serializer for list, detail delete action
    """
    class Meta:
        model = TestApp
        exclude = ('name', )
        extra_kwargs = {
            'days': {
                "error_messages": {
                    "<code>": "Error mesage",
                }
            },
        }


# Configure the  celery to send the logs in the conf file specified in logging configuration
# inside celery.py where app is configured

import celery.signals

# Logging celery logs in the file
@celery.signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    pass

# settings configurtion
# Whether to store the result and return them or Not
CELERY_TASK_IGNORE_RESULT = True
# This will store and return the result if any error occure like division by zero
CELERY_TASK_STORE_ERRORS_EVEN_IF_IGNORED = True
# This setting is used to override celery root logging setup
WORKER_HIJACK_ROOT_LOGGER = False
+ 
