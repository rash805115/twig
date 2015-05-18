import Crypto.Cipher.AES as AES
import base64

class Encryption():
	BLOCK_SIZE = 16
	PADDING = '\t'
	
	def encrypt(self, message, key):
		pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING
		EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
		secret = pad(key)
		cipher = AES.new(secret)
		return EncodeAES(cipher, message)
	
	def decrypt(self, secret, key):
		pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING
		DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode("UTF-8").rstrip(self.PADDING)
		cipher = AES.new(pad(key))
		return DecodeAES(cipher, secret)