import datetime

# Modify this date format according to your SSL certificate's format
certificate_date = '{{ cert.results[0].not_after }}'

try:
    cert_not_after_date = datetime.datetime.strptime(certificate_date, '%Y%m%d%H%M%S%z')
except ValueError:
    print("Error: Date parsing failed.")
else:
    print(f"Certificate Expiry Date: {cert_not_after_date}")
