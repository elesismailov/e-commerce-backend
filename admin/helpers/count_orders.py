
from api.models import StatusCode, Order

def count_orders():

    '''
    returns {status-code: count-of-orders, etc...}
    '''
    
    status_codes = StatusCode.objects.all()

    count = {}

    for status_code in status_codes:
        
        orders_count = Order.objects.filter(status_code=status_code).count()

        count[status_code.code] = orders_count

    return count
