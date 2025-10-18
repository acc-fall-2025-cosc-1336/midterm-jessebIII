def get_assessment_value(value):
    return value * 0.6

def get_tax_assessed(assessment_value):
    return (assessment_value/100) *0.72

# helper used by tests
def test_config():
    return True

