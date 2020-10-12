from app.Models import DemoTable

def test(request):
    print(request)
    # a = DemoTable.query.filter_by(id=1).first()
    # print(a)
    return 200, "", {}