import pyotp as pyo
import qrcode

# Generate a proper base32 key
key = pyo.random_base32()  # This generates a valid base32 secret key
print(f"Generated Secret Key: {key}")

# Create a TOTP object with the key
totp = pyo.TOTP(key)

# Generate a current OTP and display it
current_otp = totp.now()
print(f"Current OTP: {current_otp}")

# Verify an OTP (replace '861267' with the actual OTP generated for testing)
test_otp = "861267"
is_verified = totp.verify(test_otp)  # This will check if the test OTP is valid
print(f"Is the OTP '{test_otp}' verified?: {is_verified}")

# Generate a provisioning URI for the TOTP
# This is what you use to integrate with an authenticator app like Google Authenticator
provisioning_url = totp.provisioning_uri(name="JapjeevKaur", issuer_name="JapjeevAuth")
print(f"Provisioning URL: {provisioning_url}")

# HOTP Example
# Create an HOTP object with another base32 secret
hotp_key = pyo.random_base32()
hotp = pyo.HOTP(hotp_key)

# Generate HOTP codes for different counters
print(f"HOTP Key: {hotp_key}")
print(f"HOTP at counter 0: {hotp.at(0)}")
print(f"HOTP at counter 1: {hotp.at(1)}")
print(f"HOTP at counter 1401: {hotp.at(1401)}")

# Verify HOTP codes with the correct counter
print(f"Is HOTP '316439' at counter 1401 valid?: {hotp.verify('316439', 1401)}")
print(f"Is HOTP '316439' at counter 1402 valid?: {hotp.verify('316439', 1402)}")

# Generate a QR code for the provisioning URL
qr_image = qrcode.make(provisioning_url)
qr_image.show() 