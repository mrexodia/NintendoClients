
# This file was generated automatically by generate_protocols.py

from nintendo.nex import common

import logging
logger = logging.getLogger(__name__)


class MessageDeliveryProtocol:
	METHOD_DELIVER_MESSAGE = 1
	
	PROTOCOL_ID = 0x1B


class MessageDeliveryClient(MessageDeliveryProtocol):
	def __init__(self, client):
		self.client = client
	
	def deliver_message(self, message):
		logger.info("MessageDeliveryClient.deliver_message()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_DELIVER_MESSAGE)
		stream.anydata(message)
		self.client.send_message(stream)
		
		#--- response ---
		self.client.get_response(call_id)
		logger.info("MessageDeliveryClient.deliver_message -> done")


class MessageDeliveryServer(MessageDeliveryProtocol):
	def __init__(self):
		self.methods = {
			self.METHOD_DELIVER_MESSAGE: self.handle_deliver_message,
		}
	
	def handle(self, context, method_id, input, output):
		if method_id in self.methods:
			self.methods[method_id](context, input, output)
		else:
			logger.warning("Unknown method called on %s: %i", self.__class__.__name__, method_id)
			raise common.RMCError("Core::NotImplemented")
	
	def handle_deliver_message(self, context, input, output):
		logger.info("MessageDeliveryServer.deliver_message()")
		#--- request ---
		message = input.anydata()
		self.deliver_message(context, message)
	
	def deliver_message(self, *args):
		logger.warning("MessageDeliveryServer.deliver_message not implemented")
		raise common.RMCError("Core::NotImplemented")

