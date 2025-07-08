import pytest
from payments.pix import Pix

class TestPix:
   def setup_method(self):
      self.pix_instance = Pix()
   
   def test_pix_create_payment(self):
      payment_info = self.pix_instance.create_payment()

      assert payment_info is not None
      assert isinstance(payment_info, dict)
      assert 'bank_payment_id' in payment_info
      assert 'qr_code_path' in payment_info

      assert isinstance(payment_info['bank_payment_id'], str)
      assert isinstance(payment_info['qr_code_path'], str)

      print(f"Payment Created? {payment_info}")
   
   def test_pix_payment_id_format(self):
      payment_info = self.pix_instance.create_payment()
      bank_payment_id = payment_info['bank_payment_id']

      assert len(bank_payment_id) >= 30
      assert '-' in bank_payment_id
   
   def test_qr_code_path_format(self):
      payment_info = self.pix_instance.create_payment()
      qr_code_path = payment_info['qr_code_path']

      assert qr_code_path.startswith('qr_code_payment_')
      assert payment_info['bank_payment_id'] in qr_code_path

