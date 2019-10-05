
# This file was generated automatically by generate_protocols.py

from nintendo.nex import common

import logging
logger = logging.getLogger(__name__)


class CourseRecordInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.unk2 = None
		self.world_record_pid = None
		self.first_clear_pid = None
		self.world_record = None
		self.world_record_date = None
		self.first_clear_date = None
	
	def check_required(self, settings):
		for field in ['data_id', 'unk2', 'world_record_pid', 'first_clear_pid', 'world_record', 'world_record_date', 'first_clear_date']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.unk2 = stream.u8()
		self.world_record_pid = stream.pid()
		self.first_clear_pid = stream.pid()
		self.world_record = stream.u32()
		self.world_record_date = stream.datetime()
		self.first_clear_date = stream.datetime()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.u8(self.unk2)
		stream.pid(self.world_record_pid)
		stream.pid(self.first_clear_pid)
		stream.u32(self.world_record)
		stream.datetime(self.world_record_date)
		stream.datetime(self.first_clear_date)


class DataStoreChangeMetaCompareParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.comparison_flag = None
		self.name = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.period = None
		self.meta_binary = None
		self.tags = None
		self.referred_count = None
		self.data_type = None
		self.status = None
	
	def check_required(self, settings):
		for field in ['comparison_flag', 'name', 'period', 'meta_binary', 'tags', 'referred_count', 'data_type', 'status']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.comparison_flag = stream.u32()
		self.name = stream.string()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.period = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.tags = stream.list(stream.string)
		self.referred_count = stream.u32()
		self.data_type = stream.u16()
		self.status = stream.u8()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u32(self.comparison_flag)
		stream.string(self.name)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u16(self.period)
		stream.qbuffer(self.meta_binary)
		stream.list(self.tags, stream.string)
		stream.u32(self.referred_count)
		stream.u16(self.data_type)
		stream.u8(self.status)


class DataStoreChangeMetaParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.modifies_flag = None
		self.name = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.period = None
		self.meta_binary = None
		self.tags = None
		self.update_password = None
		self.referred_count = None
		self.data_type = None
		self.status = None
		self.compare_param = DataStoreChangeMetaCompareParam()
	
	def check_required(self, settings):
		for field in ['data_id', 'modifies_flag', 'name', 'period', 'meta_binary', 'tags', 'update_password', 'referred_count', 'data_type', 'status']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.modifies_flag = stream.u32()
		self.name = stream.string()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.period = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.tags = stream.list(stream.string)
		self.update_password = stream.u64()
		self.referred_count = stream.u32()
		self.data_type = stream.u16()
		self.status = stream.u8()
		self.compare_param = stream.extract(DataStoreChangeMetaCompareParam)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.u32(self.modifies_flag)
		stream.string(self.name)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u16(self.period)
		stream.qbuffer(self.meta_binary)
		stream.list(self.tags, stream.string)
		stream.u64(self.update_password)
		stream.u32(self.referred_count)
		stream.u16(self.data_type)
		stream.u8(self.status)
		stream.add(self.compare_param)


class DataStoreCompletePostParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.is_success = None
	
	def check_required(self, settings):
		for field in ['data_id', 'is_success']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.is_success = stream.bool()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.bool(self.is_success)


class DataStoreFileServerObjectInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk = None
		self.info = DataStoreReqGetInfo()
	
	def check_required(self, settings):
		for field in ['unk']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk = stream.u64()
		self.info = stream.extract(DataStoreReqGetInfo)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.unk)
		stream.add(self.info)


class DataStoreGetMetaParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = 0
		self.persistence_target = PersistenceTarget()
		self.result_option = 0
		self.access_password = 0
	
	def check_required(self, settings):
		pass
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.persistence_target = stream.extract(PersistenceTarget)
		self.result_option = stream.u8()
		self.access_password = stream.u64()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.add(self.persistence_target)
		stream.u8(self.result_option)
		stream.u64(self.access_password)


class DataStoreInfoStuff(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.stars_received = None
		self.info = DataStoreMetaInfo()
	
	def check_required(self, settings):
		for field in ['unk1', 'stars_received']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u32()
		self.stars_received = stream.u32()
		self.info = stream.extract(DataStoreMetaInfo)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u32(self.unk1)
		stream.u32(self.stars_received)
		stream.add(self.info)


class DataStoreKeyValue(common.Structure):
	def __init__(self):
		super().__init__()
		self.key = None
		self.value = None
	
	def check_required(self, settings):
		for field in ['key', 'value']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.key = stream.string()
		self.value = stream.string()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.string(self.key)
		stream.string(self.value)


class DataStoreMetaInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.owner_id = None
		self.size = None
		self.name = None
		self.data_type = None
		self.meta_binary = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.create_time = None
		self.update_time = None
		self.period = None
		self.status = None
		self.referred_count = None
		self.refer_data_id = None
		self.flag = None
		self.referred_time = None
		self.expire_time = None
		self.tags = None
		self.ratings = None
	
	def check_required(self, settings):
		for field in ['data_id', 'owner_id', 'size', 'name', 'data_type', 'meta_binary', 'create_time', 'update_time', 'period', 'status', 'referred_count', 'refer_data_id', 'flag', 'referred_time', 'expire_time', 'tags', 'ratings']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.owner_id = stream.pid()
		self.size = stream.u32()
		self.name = stream.string()
		self.data_type = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.create_time = stream.datetime()
		self.update_time = stream.datetime()
		self.period = stream.u16()
		self.status = stream.u8()
		self.referred_count = stream.u32()
		self.refer_data_id = stream.u32()
		self.flag = stream.u32()
		self.referred_time = stream.datetime()
		self.expire_time = stream.datetime()
		self.tags = stream.list(stream.string)
		self.ratings = stream.list(DataStoreRatingInfoWithSlot)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.pid(self.owner_id)
		stream.u32(self.size)
		stream.string(self.name)
		stream.u16(self.data_type)
		stream.qbuffer(self.meta_binary)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.datetime(self.create_time)
		stream.datetime(self.update_time)
		stream.u16(self.period)
		stream.u8(self.status)
		stream.u32(self.referred_count)
		stream.u32(self.refer_data_id)
		stream.u32(self.flag)
		stream.datetime(self.referred_time)
		stream.datetime(self.expire_time)
		stream.list(self.tags, stream.string)
		stream.list(self.ratings, stream.add)


class DataStorePermission(common.Structure):
	def __init__(self):
		super().__init__()
		self.permission = None
		self.recipients = None
	
	def check_required(self, settings):
		for field in ['permission', 'recipients']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.permission = stream.u8()
		self.recipients = stream.list(stream.pid)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u8(self.permission)
		stream.list(self.recipients, stream.pid)


class DataStorePersistenceInitParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.persistence_slot_id = None
		self.delete_last_object = None
	
	def check_required(self, settings):
		for field in ['persistence_slot_id', 'delete_last_object']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.persistence_slot_id = stream.u16()
		self.delete_last_object = stream.bool()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u16(self.persistence_slot_id)
		stream.bool(self.delete_last_object)


class DataStorePrepareGetParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = 0
		self.lock_id = 0
		self.persistence_target = PersistenceTarget()
		self.access_password = 0
		self.extra_data = None
	
	def check_required(self, settings):
		for field in ['extra_data']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.lock_id = stream.u32()
		self.persistence_target = stream.extract(PersistenceTarget)
		self.access_password = stream.u64()
		self.extra_data = stream.list(stream.string)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.u32(self.lock_id)
		stream.add(self.persistence_target)
		stream.u64(self.access_password)
		stream.list(self.extra_data, stream.string)


class DataStorePreparePostParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.size = None
		self.name = None
		self.data_type = None
		self.meta_binary = None
		self.permission = DataStorePermission()
		self.delete_permission = DataStorePermission()
		self.flag = None
		self.period = None
		self.refer_data_id = None
		self.tags = None
		self.rating_init_params = None
		self.persistence_init_param = DataStorePersistenceInitParam()
		self.extra_data = None
	
	def check_required(self, settings):
		for field in ['size', 'name', 'data_type', 'meta_binary', 'flag', 'period', 'refer_data_id', 'tags', 'rating_init_params', 'extra_data']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.size = stream.u32()
		self.name = stream.string()
		self.data_type = stream.u16()
		self.meta_binary = stream.qbuffer()
		self.permission = stream.extract(DataStorePermission)
		self.delete_permission = stream.extract(DataStorePermission)
		self.flag = stream.u32()
		self.period = stream.u16()
		self.refer_data_id = stream.u32()
		self.tags = stream.list(stream.string)
		self.rating_init_params = stream.list(DataStoreRatingInitParamWithSlot)
		self.persistence_init_param = stream.extract(DataStorePersistenceInitParam)
		self.extra_data = stream.list(stream.string)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u32(self.size)
		stream.string(self.name)
		stream.u16(self.data_type)
		stream.qbuffer(self.meta_binary)
		stream.add(self.permission)
		stream.add(self.delete_permission)
		stream.u32(self.flag)
		stream.u16(self.period)
		stream.u32(self.refer_data_id)
		stream.list(self.tags, stream.string)
		stream.list(self.rating_init_params, stream.add)
		stream.add(self.persistence_init_param)
		stream.list(self.extra_data, stream.string)


class DataStoreRateObjectParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.rating_value = None
		self.access_password = None
	
	def check_required(self, settings):
		for field in ['rating_value', 'access_password']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.rating_value = stream.s32()
		self.access_password = stream.u64()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.s32(self.rating_value)
		stream.u64(self.access_password)


class DataStoreRatingInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.total_value = None
		self.count = None
		self.initial_value = None
	
	def check_required(self, settings):
		for field in ['total_value', 'count', 'initial_value']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.total_value = stream.s64()
		self.count = stream.u32()
		self.initial_value = stream.s64()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.s64(self.total_value)
		stream.u32(self.count)
		stream.s64(self.initial_value)


class DataStoreRatingInfoWithSlot(common.Structure):
	def __init__(self):
		super().__init__()
		self.slot = None
		self.info = DataStoreRatingInfo()
	
	def check_required(self, settings):
		for field in ['slot']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.slot = stream.u8()
		self.info = stream.extract(DataStoreRatingInfo)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u8(self.slot)
		stream.add(self.info)


class DataStoreRatingInitParam(common.Structure):
	def __init__(self):
		super().__init__()
		self.flag = None
		self.internal_flag = None
		self.lock_type = None
		self.initial_value = None
		self.range_min = None
		self.range_max = None
		self.period_hour = None
		self.period_duration = None
	
	def check_required(self, settings):
		for field in ['flag', 'internal_flag', 'lock_type', 'initial_value', 'range_min', 'range_max', 'period_hour', 'period_duration']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.flag = stream.u8()
		self.internal_flag = stream.u8()
		self.lock_type = stream.u8()
		self.initial_value = stream.s64()
		self.range_min = stream.s32()
		self.range_max = stream.s32()
		self.period_hour = stream.s8()
		self.period_duration = stream.s16()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u8(self.flag)
		stream.u8(self.internal_flag)
		stream.u8(self.lock_type)
		stream.s64(self.initial_value)
		stream.s32(self.range_min)
		stream.s32(self.range_max)
		stream.s8(self.period_hour)
		stream.s16(self.period_duration)


class DataStoreRatingInitParamWithSlot(common.Structure):
	def __init__(self):
		super().__init__()
		self.slot = None
		self.param = DataStoreRatingInitParam()
	
	def check_required(self, settings):
		for field in ['slot']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.slot = stream.s8()
		self.param = stream.extract(DataStoreRatingInitParam)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.s8(self.slot)
		stream.add(self.param)


class DataStoreRatingTarget(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.slot = None
	
	def check_required(self, settings):
		for field in ['data_id', 'slot']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.slot = stream.s8()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.s8(self.slot)


class DataStoreReqGetInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.url = None
		self.headers = None
		self.size = None
		self.root_ca_cert = None
		self.data_id = None
	
	def check_required(self, settings):
		for field in ['url', 'headers', 'size', 'root_ca_cert', 'data_id']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.url = stream.string()
		self.headers = stream.list(DataStoreKeyValue)
		self.size = stream.u32()
		self.root_ca_cert = stream.buffer()
		self.data_id = stream.u64()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.string(self.url)
		stream.list(self.headers, stream.add)
		stream.u32(self.size)
		stream.buffer(self.root_ca_cert)
		stream.u64(self.data_id)


class DataStoreReqPostInfo(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.url = None
		self.headers = None
		self.form = None
		self.root_ca_cert = None
	
	def check_required(self, settings):
		for field in ['data_id', 'url', 'headers', 'form', 'root_ca_cert']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.url = stream.string()
		self.headers = stream.list(DataStoreKeyValue)
		self.form = stream.list(DataStoreKeyValue)
		self.root_ca_cert = stream.buffer()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.string(self.url)
		stream.list(self.headers, stream.add)
		stream.list(self.form, stream.add)
		stream.buffer(self.root_ca_cert)


class MethodParam49(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = UnknownStruct5()
		self.unk3 = None
		self.unk4 = UnknownStruct()
	
	def check_required(self, settings):
		for field in ['unk1', 'unk3']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u32()
		self.unk2 = stream.extract(UnknownStruct5)
		self.unk3 = stream.u8()
		self.unk4 = stream.extract(UnknownStruct)
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u32(self.unk1)
		stream.add(self.unk2)
		stream.u8(self.unk3)
		stream.add(self.unk4)


class MethodParam50(common.Structure):
	def __init__(self):
		super().__init__()
		self.magic = None
		self.data_ids = None
		self.unk = None
	
	def check_required(self, settings):
		for field in ['magic', 'data_ids', 'unk']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.magic = stream.u32()
		self.data_ids = stream.list(stream.u64)
		self.unk = stream.u8()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u32(self.magic)
		stream.list(self.data_ids, stream.u64)
		stream.u8(self.unk)


class MethodParam59(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = DataStorePreparePostParam()
		self.unk2 = None
		self.unk3 = None
	
	def check_required(self, settings):
		for field in ['unk2', 'unk3']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.extract(DataStorePreparePostParam)
		self.unk2 = stream.u64()
		self.unk3 = stream.string()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.add(self.unk1)
		stream.u64(self.unk2)
		stream.string(self.unk3)


class MethodParam71(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
		self.unk3 = None
	
	def check_required(self, settings):
		for field in ['unk1', 'unk2', 'unk3']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u64()
		self.unk2 = stream.u8()
		self.unk3 = stream.u32()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.unk1)
		stream.u8(self.unk2)
		stream.u32(self.unk3)


class MethodParam87(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
		self.unk3 = None
		self.unk4 = None
	
	def check_required(self, settings):
		for field in ['unk1', 'unk2', 'unk3', 'unk4']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u64()
		self.unk2 = stream.string()
		self.unk3 = stream.u8()
		self.unk4 = stream.string()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.unk1)
		stream.string(self.unk2)
		stream.u8(self.unk3)
		stream.string(self.unk4)


class PersistenceTarget(common.Structure):
	def __init__(self):
		super().__init__()
		self.owner_id = 0
		self.persistence_id = 65535
	
	def check_required(self, settings):
		pass
	
	def load(self, stream):
		self.owner_id = stream.pid()
		self.persistence_id = stream.u16()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.pid(self.owner_id)
		stream.u16(self.persistence_id)


class UnknownStruct(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
	
	def check_required(self, settings):
		for field in ['unk1', 'unk2']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u32()
		self.unk2 = stream.u32()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u32(self.unk1)
		stream.u32(self.unk2)


class UnknownStruct2(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.unk2 = None
	
	def check_required(self, settings):
		for field in ['data_id', 'unk2']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.unk2 = stream.u8()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.u8(self.unk2)


class UnknownStruct3(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
		self.unk3 = None
		self.unk4 = None
		self.unk5 = None
		self.unk6 = None
		self.unk7 = None
	
	def check_required(self, settings):
		for field in ['unk1', 'unk2', 'unk3', 'unk4', 'unk5', 'unk6', 'unk7']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u64()
		self.unk2 = stream.u8()
		self.unk3 = stream.u32()
		self.unk4 = stream.u32()
		self.unk5 = stream.u32()
		self.unk6 = stream.datetime()
		self.unk7 = stream.datetime()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.unk1)
		stream.u8(self.unk2)
		stream.u32(self.unk3)
		stream.u32(self.unk4)
		stream.u32(self.unk5)
		stream.datetime(self.unk6)
		stream.datetime(self.unk7)


class UnknownStruct4(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.unk2 = None
	
	def check_required(self, settings):
		for field in ['data_id', 'unk2']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.unk2 = stream.u32()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.u32(self.unk2)


class UnknownStruct5(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.unk2 = None
		self.unk3 = None
	
	def check_required(self, settings):
		for field in ['unk1', 'unk2', 'unk3']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u8()
		self.unk2 = stream.u32()
		self.unk3 = stream.u32()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u8(self.unk1)
		stream.u32(self.unk2)
		stream.u32(self.unk3)


class UnknownStruct6(common.Structure):
	def __init__(self):
		super().__init__()
		self.data_id = None
		self.unk2 = None
		self.unk3 = None
		self.unk4 = None
	
	def check_required(self, settings):
		for field in ['data_id', 'unk2', 'unk3', 'unk4']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.data_id = stream.u64()
		self.unk2 = stream.u32()
		self.unk3 = stream.u32()
		self.unk4 = stream.u16()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u64(self.data_id)
		stream.u32(self.unk2)
		stream.u32(self.unk3)
		stream.u16(self.unk4)


class UnknownStruct7(common.Structure):
	def __init__(self):
		super().__init__()
		self.unk1 = None
		self.pids = None
		self.unk3 = None
		self.unk4 = None
		self.unk5 = None
		self.unk6 = None
		self.unk7 = None
		self.unk8 = None
		self.unk9 = None
		self.unk10 = None
		self.unk11 = None
		self.unk12 = None
		self.unk13 = None
		self.unk14 = UnknownStruct()
		self.unk15 = None
		self.unk16 = None
		self.unk17 = None
	
	def get_version(self, settings):
		version = 0
		version = 1
		return version
	
	def check_required(self, settings):
		for field in ['unk1', 'pids', 'unk3', 'unk4', 'unk5', 'unk6', 'unk7', 'unk8', 'unk9', 'unk10', 'unk11', 'unk12', 'unk13', 'unk15', 'unk16', 'unk17']:
			if getattr(self, field) is None:
				raise ValueError("No value assigned to required field: %s" %field)
	
	def load(self, stream):
		self.unk1 = stream.u8()
		self.pids = stream.list(stream.pid)
		self.unk3 = stream.u8()
		self.unk4 = stream.list(stream.u32)
		self.unk5 = stream.u16()
		self.unk6 = stream.datetime()
		self.unk7 = stream.datetime()
		self.unk8 = stream.datetime()
		self.unk9 = stream.datetime()
		self.unk10 = stream.u32()
		self.unk11 = stream.list(stream.string)
		self.unk12 = stream.u8()
		self.unk13 = stream.u8()
		self.unk14 = stream.extract(UnknownStruct)
		self.unk15 = stream.u8()
		self.unk16 = stream.u32()
		self.unk17 = stream.bool()
	
	def save(self, stream):
		self.check_required(stream.settings)
		stream.u8(self.unk1)
		stream.list(self.pids, stream.pid)
		stream.u8(self.unk3)
		stream.list(self.unk4, stream.u32)
		stream.u16(self.unk5)
		stream.datetime(self.unk6)
		stream.datetime(self.unk7)
		stream.datetime(self.unk8)
		stream.datetime(self.unk9)
		stream.u32(self.unk10)
		stream.list(self.unk11, stream.string)
		stream.u8(self.unk12)
		stream.u8(self.unk13)
		stream.add(self.unk14)
		stream.u8(self.unk15)
		stream.u32(self.unk16)
		stream.bool(self.unk17)


class DataStoreSmmProtocol:
	METHOD_GET_META = 8
	METHOD_PREPARE_POST_OBJECT = 24
	METHOD_PREPARE_GET_OBJECT = 25
	METHOD_COMPLETE_POST_OBJECT = 26
	METHOD_GET_METAS_MULTIPLE_PARAM = 36
	METHOD_CHANGE_META = 38
	METHOD_RATE_OBJECTS = 40
	METHOD_GET_FILE_SERVER_OBJECT_INFOS = 45
	METHOD_RATE_CUSTOM_RANKING = 48
	METHOD_METHOD49 = 49
	METHOD_GET_CUSTOM_RANKING_BY_DATA_ID = 50
	METHOD_ADD_TO_BUFFER_QUEUE = 52
	METHOD_ADD_TO_BUFFER_QUEUES = 53
	METHOD_GET_BUFFER_QUEUE = 54
	METHOD_GET_BUFFER_QUEUES = 55
	METHOD_CLEAR_BUFFER_QUEUES = 56
	METHOD_COMPLETE_ATTACH_FILE = 57
	METHOD_COMPLETE_ATTACH_FILE_V1 = 58
	METHOD_PREPARE_ATTACH_FILE = 59
	METHOD_CONDITIONAL_SEARCH_OBJECT = 60
	METHOD_GET_APPLICATION_CONFIG = 61
	METHOD_SET_APPLICATION_CONFIG = 62
	METHOD_DELETE_APPLICATION_CONFIG = 63
	METHOD_LATEST_COURSE_SEARCH_OBJECT = 64
	METHOD_FOLLOWINGS_LATEST_COURSE_SEARCH_OBJECT = 65
	METHOD_RECOMMENDED_COURSE_SEARCH_OBJECT = 66
	METHOD_SCORE_RANGE_CASCADED_SEARCH_OBJECT = 67
	METHOD_SUGGESTED_COURSE_SEARCH_OBJECT = 68
	METHOD_UPLOAD_COURSE_RECORD = 71
	METHOD_GET_COURSE_RECORD = 72
	METHOD_DELETE_COURSE_RECORD = 73
	METHOD_GET_APPLICATION_CONFIG_STRING = 74
	METHOD_SET_APPLICATION_CONFIG_STRING = 75
	METHOD_GET_DELETION_REASON = 76
	METHOD_SET_DELETION_REASON = 77
	METHOD_GET_METAS_WITH_COURSE_RECORD = 78
	METHOD_CHECK_RATE_CUSTOM_RANKING_COUNTER = 79
	METHOD_RESET_RATE_CUSTOM_RANKING_COUNTER = 80
	METHOD_BEST_SCORE_RATE_COURSE_SEARCH_OBJECT = 81
	METHOD_CTR_PICK_UP_COURSE_SEARCH_OBJECT = 82
	METHOD_SEARCH_UNKNOWN_PLATFORM_OBJECTS = 86
	METHOD_REPORT_COURSE = 87
	
	PROTOCOL_ID = 0x73


class DataStoreSmmClient(DataStoreSmmProtocol):
	def __init__(self, client):
		self.client = client
	
	def get_meta(self, param):
		logger.info("DataStoreSmmClient.get_meta()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_META)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		info = stream.extract(DataStoreMetaInfo)
		logger.info("DataStoreSmmClient.get_meta -> done")
		return info
	
	def prepare_post_object(self, param):
		logger.info("DataStoreSmmClient.prepare_post_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_PREPARE_POST_OBJECT)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		info = stream.extract(DataStoreReqPostInfo)
		logger.info("DataStoreSmmClient.prepare_post_object -> done")
		return info
	
	def prepare_get_object(self, param):
		logger.info("DataStoreSmmClient.prepare_get_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_PREPARE_GET_OBJECT)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		info = stream.extract(DataStoreReqGetInfo)
		logger.info("DataStoreSmmClient.prepare_get_object -> done")
		return info
	
	def complete_post_object(self, param):
		logger.info("DataStoreSmmClient.complete_post_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_COMPLETE_POST_OBJECT)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		self.client.get_response(call_id)
		logger.info("DataStoreSmmClient.complete_post_object -> done")
	
	def get_metas_multiple_param(self, params):
		logger.info("DataStoreSmmClient.get_metas_multiple_param()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_METAS_MULTIPLE_PARAM)
		stream.list(params, stream.add)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		obj = common.RMCResponse()
		obj.infos = stream.list(DataStoreMetaInfo)
		obj.results = stream.list(stream.result)
		logger.info("DataStoreSmmClient.get_metas_multiple_param -> done")
		return obj
	
	def change_meta(self, param):
		logger.info("DataStoreSmmClient.change_meta()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_CHANGE_META)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		self.client.get_response(call_id)
		logger.info("DataStoreSmmClient.change_meta -> done")
	
	def rate_objects(self, targets, params, transactional, fetch_ratings):
		logger.info("DataStoreSmmClient.rate_objects()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_RATE_OBJECTS)
		stream.list(targets, stream.add)
		stream.list(params, stream.add)
		stream.bool(transactional)
		stream.bool(fetch_ratings)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		obj = common.RMCResponse()
		obj.ratings = stream.list(DataStoreRatingInfo)
		obj.results = stream.list(stream.result)
		logger.info("DataStoreSmmClient.rate_objects -> done")
		return obj
	
	def get_file_server_object_infos(self, object_ids):
		logger.info("DataStoreSmmClient.get_file_server_object_infos()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_FILE_SERVER_OBJECT_INFOS)
		stream.list(object_ids, stream.u64)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreFileServerObjectInfo)
		logger.info("DataStoreSmmClient.get_file_server_object_infos -> done")
		return infos
	
	def rate_custom_ranking(self, param):
		logger.info("DataStoreSmmClient.rate_custom_ranking()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_RATE_CUSTOM_RANKING)
		stream.list(param, stream.add)
		self.client.send_message(stream)
		
		#--- response ---
		self.client.get_response(call_id)
		logger.info("DataStoreSmmClient.rate_custom_ranking -> done")
	
	def method49(self, param):
		logger.info("DataStoreSmmClient.method49()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_METHOD49)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		obj = common.RMCResponse()
		obj.infos = stream.list(DataStoreInfoStuff)
		obj.results = stream.list(stream.result)
		logger.info("DataStoreSmmClient.method49 -> done")
		return obj
	
	def get_custom_ranking_by_data_id(self, param):
		logger.info("DataStoreSmmClient.get_custom_ranking_by_data_id()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_CUSTOM_RANKING_BY_DATA_ID)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		obj = common.RMCResponse()
		obj.infos = stream.list(DataStoreInfoStuff)
		obj.results = stream.list(stream.result)
		logger.info("DataStoreSmmClient.get_custom_ranking_by_data_id -> done")
		return obj
	
	def add_to_buffer_queues(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.add_to_buffer_queues()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_ADD_TO_BUFFER_QUEUES)
		stream.list(unknown1, stream.add)
		stream.list(unknown2, stream.qbuffer)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		results = stream.list(stream.result)
		logger.info("DataStoreSmmClient.add_to_buffer_queues -> done")
		return results
	
	def get_buffer_queue(self, param):
		logger.info("DataStoreSmmClient.get_buffer_queue()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_BUFFER_QUEUE)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		results = stream.list(stream.qbuffer)
		logger.info("DataStoreSmmClient.get_buffer_queue -> done")
		return results
	
	def complete_attach_file(self, param):
		logger.info("DataStoreSmmClient.complete_attach_file()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_COMPLETE_ATTACH_FILE)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		unknown = stream.string()
		logger.info("DataStoreSmmClient.complete_attach_file -> done")
		return unknown
	
	def prepare_attach_file(self, param):
		logger.info("DataStoreSmmClient.prepare_attach_file()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_PREPARE_ATTACH_FILE)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.extract(DataStoreReqPostInfo)
		logger.info("DataStoreSmmClient.prepare_attach_file -> done")
		return infos
	
	def conditional_search_object(self, unknown1, unknown2, unknown3):
		logger.info("DataStoreSmmClient.conditional_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_CONDITIONAL_SEARCH_OBJECT)
		stream.u32(unknown1)
		stream.add(unknown2)
		stream.list(unknown3, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		info = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.conditional_search_object -> done")
		return info
	
	def get_application_config(self, param):
		logger.info("DataStoreSmmClient.get_application_config()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_APPLICATION_CONFIG)
		stream.u32(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		unknown = stream.list(stream.u32)
		logger.info("DataStoreSmmClient.get_application_config -> done")
		return unknown
	
	def latest_course_search_object(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.latest_course_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_LATEST_COURSE_SEARCH_OBJECT)
		stream.add(unknown1)
		stream.list(unknown2, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.latest_course_search_object -> done")
		return infos
	
	def followings_latest_course_search_object(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.followings_latest_course_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_FOLLOWINGS_LATEST_COURSE_SEARCH_OBJECT)
		stream.add(unknown1)
		stream.list(unknown2, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.followings_latest_course_search_object -> done")
		return infos
	
	def recommended_course_search_object(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.recommended_course_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_RECOMMENDED_COURSE_SEARCH_OBJECT)
		stream.add(unknown1)
		stream.list(unknown2, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.recommended_course_search_object -> done")
		return infos
	
	def score_range_cascaded_search_object(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.score_range_cascaded_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_SCORE_RANGE_CASCADED_SEARCH_OBJECT)
		stream.add(unknown1)
		stream.list(unknown2, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.score_range_cascaded_search_object -> done")
		return infos
	
	def suggested_course_search_object(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.suggested_course_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_SUGGESTED_COURSE_SEARCH_OBJECT)
		stream.add(unknown1)
		stream.list(unknown2, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.suggested_course_search_object -> done")
		return infos
	
	def upload_course_record(self, param):
		logger.info("DataStoreSmmClient.upload_course_record()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_UPLOAD_COURSE_RECORD)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		self.client.get_response(call_id)
		logger.info("DataStoreSmmClient.upload_course_record -> done")
	
	def get_course_record(self, param):
		logger.info("DataStoreSmmClient.get_course_record()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_COURSE_RECORD)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		unknown = stream.extract(CourseRecordInfo)
		logger.info("DataStoreSmmClient.get_course_record -> done")
		return unknown
	
	def get_application_config_string(self, param):
		logger.info("DataStoreSmmClient.get_application_config_string()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_APPLICATION_CONFIG_STRING)
		stream.u32(param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		unknown = stream.list(stream.string)
		logger.info("DataStoreSmmClient.get_application_config_string -> done")
		return unknown
	
	def get_deletion_reason(self, unknown):
		logger.info("DataStoreSmmClient.get_deletion_reason()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_DELETION_REASON)
		stream.list(unknown, stream.u64)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		unknown = stream.list(stream.u32)
		logger.info("DataStoreSmmClient.get_deletion_reason -> done")
		return unknown
	
	def get_metas_with_course_record(self, unknown, get_meta_param):
		logger.info("DataStoreSmmClient.get_metas_with_course_record()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_GET_METAS_WITH_COURSE_RECORD)
		stream.list(unknown, stream.add)
		stream.add(get_meta_param)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		obj = common.RMCResponse()
		obj.infos = stream.list(DataStoreMetaInfo)
		obj.unknown = stream.list(CourseRecordInfo)
		obj.results = stream.list(stream.result)
		logger.info("DataStoreSmmClient.get_metas_with_course_record -> done")
		return obj
	
	def check_rate_custom_ranking_counter(self, unk1):
		logger.info("DataStoreSmmClient.check_rate_custom_ranking_counter()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_CHECK_RATE_CUSTOM_RANKING_COUNTER)
		stream.u32(unk1)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		result = stream.bool()
		logger.info("DataStoreSmmClient.check_rate_custom_ranking_counter -> done")
		return result
	
	def best_score_rate_course_search_object(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.best_score_rate_course_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_BEST_SCORE_RATE_COURSE_SEARCH_OBJECT)
		stream.add(unknown1)
		stream.list(unknown2, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.best_score_rate_course_search_object -> done")
		return infos
	
	def ctr_pick_up_course_search_object(self, unknown1, unknown2):
		logger.info("DataStoreSmmClient.ctr_pick_up_course_search_object()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_CTR_PICK_UP_COURSE_SEARCH_OBJECT)
		stream.add(unknown1)
		stream.list(unknown2, stream.string)
		self.client.send_message(stream)
		
		#--- response ---
		stream = self.client.get_response(call_id)
		infos = stream.list(DataStoreInfoStuff)
		logger.info("DataStoreSmmClient.ctr_pick_up_course_search_object -> done")
		return infos
	
	def report_course(self, param):
		logger.info("DataStoreSmmClient.report_course()")
		#--- request ---
		stream, call_id = self.client.init_request(self.PROTOCOL_ID, self.METHOD_REPORT_COURSE)
		stream.add(param)
		self.client.send_message(stream)
		
		#--- response ---
		self.client.get_response(call_id)
		logger.info("DataStoreSmmClient.report_course -> done")


class DataStoreSmmServer(DataStoreSmmProtocol):
	def __init__(self):
		self.methods = {
			self.METHOD_GET_META: self.handle_get_meta,
			self.METHOD_PREPARE_POST_OBJECT: self.handle_prepare_post_object,
			self.METHOD_PREPARE_GET_OBJECT: self.handle_prepare_get_object,
			self.METHOD_COMPLETE_POST_OBJECT: self.handle_complete_post_object,
			self.METHOD_GET_METAS_MULTIPLE_PARAM: self.handle_get_metas_multiple_param,
			self.METHOD_CHANGE_META: self.handle_change_meta,
			self.METHOD_RATE_OBJECTS: self.handle_rate_objects,
			self.METHOD_GET_FILE_SERVER_OBJECT_INFOS: self.handle_get_file_server_object_infos,
			self.METHOD_RATE_CUSTOM_RANKING: self.handle_rate_custom_ranking,
			self.METHOD_METHOD49: self.handle_method49,
			self.METHOD_GET_CUSTOM_RANKING_BY_DATA_ID: self.handle_get_custom_ranking_by_data_id,
			self.METHOD_ADD_TO_BUFFER_QUEUE: self.handle_add_to_buffer_queue,
			self.METHOD_ADD_TO_BUFFER_QUEUES: self.handle_add_to_buffer_queues,
			self.METHOD_GET_BUFFER_QUEUE: self.handle_get_buffer_queue,
			self.METHOD_GET_BUFFER_QUEUES: self.handle_get_buffer_queues,
			self.METHOD_CLEAR_BUFFER_QUEUES: self.handle_clear_buffer_queues,
			self.METHOD_COMPLETE_ATTACH_FILE: self.handle_complete_attach_file,
			self.METHOD_COMPLETE_ATTACH_FILE_V1: self.handle_complete_attach_file_v1,
			self.METHOD_PREPARE_ATTACH_FILE: self.handle_prepare_attach_file,
			self.METHOD_CONDITIONAL_SEARCH_OBJECT: self.handle_conditional_search_object,
			self.METHOD_GET_APPLICATION_CONFIG: self.handle_get_application_config,
			self.METHOD_SET_APPLICATION_CONFIG: self.handle_set_application_config,
			self.METHOD_DELETE_APPLICATION_CONFIG: self.handle_delete_application_config,
			self.METHOD_LATEST_COURSE_SEARCH_OBJECT: self.handle_latest_course_search_object,
			self.METHOD_FOLLOWINGS_LATEST_COURSE_SEARCH_OBJECT: self.handle_followings_latest_course_search_object,
			self.METHOD_RECOMMENDED_COURSE_SEARCH_OBJECT: self.handle_recommended_course_search_object,
			self.METHOD_SCORE_RANGE_CASCADED_SEARCH_OBJECT: self.handle_score_range_cascaded_search_object,
			self.METHOD_SUGGESTED_COURSE_SEARCH_OBJECT: self.handle_suggested_course_search_object,
			self.METHOD_UPLOAD_COURSE_RECORD: self.handle_upload_course_record,
			self.METHOD_GET_COURSE_RECORD: self.handle_get_course_record,
			self.METHOD_DELETE_COURSE_RECORD: self.handle_delete_course_record,
			self.METHOD_GET_APPLICATION_CONFIG_STRING: self.handle_get_application_config_string,
			self.METHOD_SET_APPLICATION_CONFIG_STRING: self.handle_set_application_config_string,
			self.METHOD_GET_DELETION_REASON: self.handle_get_deletion_reason,
			self.METHOD_SET_DELETION_REASON: self.handle_set_deletion_reason,
			self.METHOD_GET_METAS_WITH_COURSE_RECORD: self.handle_get_metas_with_course_record,
			self.METHOD_CHECK_RATE_CUSTOM_RANKING_COUNTER: self.handle_check_rate_custom_ranking_counter,
			self.METHOD_RESET_RATE_CUSTOM_RANKING_COUNTER: self.handle_reset_rate_custom_ranking_counter,
			self.METHOD_BEST_SCORE_RATE_COURSE_SEARCH_OBJECT: self.handle_best_score_rate_course_search_object,
			self.METHOD_CTR_PICK_UP_COURSE_SEARCH_OBJECT: self.handle_ctr_pick_up_course_search_object,
			self.METHOD_SEARCH_UNKNOWN_PLATFORM_OBJECTS: self.handle_search_unknown_platform_objects,
			self.METHOD_REPORT_COURSE: self.handle_report_course,
		}
	
	def handle(self, context, method_id, input, output):
		if method_id in self.methods:
			self.methods[method_id](context, input, output)
		else:
			logger.warning("Unknown method called on %s: %i", self.__class__.__name__, method_id)
			raise common.RMCError("Core::NotImplemented")
	
	def handle_get_meta(self, context, input, output):
		logger.info("DataStoreSmmServer.get_meta()")
		#--- request ---
		param = input.extract(DataStoreGetMetaParam)
		response = self.get_meta(context, param)
		
		#--- response ---
		if not isinstance(response, DataStoreMetaInfo):
			raise RuntimeError("Expected DataStoreMetaInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	def handle_prepare_post_object(self, context, input, output):
		logger.info("DataStoreSmmServer.prepare_post_object()")
		#--- request ---
		param = input.extract(DataStorePreparePostParam)
		response = self.prepare_post_object(context, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqPostInfo):
			raise RuntimeError("Expected DataStoreReqPostInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	def handle_prepare_get_object(self, context, input, output):
		logger.info("DataStoreSmmServer.prepare_get_object()")
		#--- request ---
		param = input.extract(DataStorePrepareGetParam)
		response = self.prepare_get_object(context, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqGetInfo):
			raise RuntimeError("Expected DataStoreReqGetInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	def handle_complete_post_object(self, context, input, output):
		logger.info("DataStoreSmmServer.complete_post_object()")
		#--- request ---
		param = input.extract(DataStoreCompletePostParam)
		self.complete_post_object(context, param)
	
	def handle_get_metas_multiple_param(self, context, input, output):
		logger.info("DataStoreSmmServer.get_metas_multiple_param()")
		#--- request ---
		params = input.list(DataStoreGetMetaParam)
		response = self.get_metas_multiple_param(context, params)
		
		#--- response ---
		if not isinstance(response, common.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	def handle_change_meta(self, context, input, output):
		logger.info("DataStoreSmmServer.change_meta()")
		#--- request ---
		param = input.extract(DataStoreChangeMetaParam)
		self.change_meta(context, param)
	
	def handle_rate_objects(self, context, input, output):
		logger.info("DataStoreSmmServer.rate_objects()")
		#--- request ---
		targets = input.list(DataStoreRatingTarget)
		params = input.list(DataStoreRateObjectParam)
		transactional = input.bool()
		fetch_ratings = input.bool()
		response = self.rate_objects(context, targets, params, transactional, fetch_ratings)
		
		#--- response ---
		if not isinstance(response, common.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['ratings', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.ratings, output.add)
		output.list(response.results, output.result)
	
	def handle_get_file_server_object_infos(self, context, input, output):
		logger.info("DataStoreSmmServer.get_file_server_object_infos()")
		#--- request ---
		object_ids = input.list(input.u64)
		response = self.get_file_server_object_infos(context, object_ids)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_rate_custom_ranking(self, context, input, output):
		logger.info("DataStoreSmmServer.rate_custom_ranking()")
		#--- request ---
		param = input.list(UnknownStruct6)
		self.rate_custom_ranking(context, param)
	
	def handle_method49(self, context, input, output):
		logger.info("DataStoreSmmServer.method49()")
		#--- request ---
		param = input.extract(MethodParam49)
		response = self.method49(context, param)
		
		#--- response ---
		if not isinstance(response, common.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	def handle_get_custom_ranking_by_data_id(self, context, input, output):
		logger.info("DataStoreSmmServer.get_custom_ranking_by_data_id()")
		#--- request ---
		param = input.extract(MethodParam50)
		response = self.get_custom_ranking_by_data_id(context, param)
		
		#--- response ---
		if not isinstance(response, common.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.results, output.result)
	
	def handle_add_to_buffer_queue(self, context, input, output):
		logger.warning("DataStoreSmmServer.add_to_buffer_queue is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_add_to_buffer_queues(self, context, input, output):
		logger.info("DataStoreSmmServer.add_to_buffer_queues()")
		#--- request ---
		unknown1 = input.list(UnknownStruct4)
		unknown2 = input.list(input.qbuffer)
		response = self.add_to_buffer_queues(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.result)
	
	def handle_get_buffer_queue(self, context, input, output):
		logger.info("DataStoreSmmServer.get_buffer_queue()")
		#--- request ---
		param = input.extract(UnknownStruct4)
		response = self.get_buffer_queue(context, param)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.qbuffer)
	
	def handle_get_buffer_queues(self, context, input, output):
		logger.warning("DataStoreSmmServer.get_buffer_queues is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_clear_buffer_queues(self, context, input, output):
		logger.warning("DataStoreSmmServer.clear_buffer_queues is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_complete_attach_file(self, context, input, output):
		logger.info("DataStoreSmmServer.complete_attach_file()")
		#--- request ---
		param = input.extract(DataStoreCompletePostParam)
		response = self.complete_attach_file(context, param)
		
		#--- response ---
		if not isinstance(response, str):
			raise RuntimeError("Expected str, got %s" %response.__class__.__name__)
		output.string(response)
	
	def handle_complete_attach_file_v1(self, context, input, output):
		logger.warning("DataStoreSmmServer.complete_attach_file_v1 is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_prepare_attach_file(self, context, input, output):
		logger.info("DataStoreSmmServer.prepare_attach_file()")
		#--- request ---
		param = input.extract(MethodParam59)
		response = self.prepare_attach_file(context, param)
		
		#--- response ---
		if not isinstance(response, DataStoreReqPostInfo):
			raise RuntimeError("Expected DataStoreReqPostInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	def handle_conditional_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.conditional_search_object()")
		#--- request ---
		unknown1 = input.u32()
		unknown2 = input.extract(UnknownStruct7)
		unknown3 = input.list(input.string)
		response = self.conditional_search_object(context, unknown1, unknown2, unknown3)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_get_application_config(self, context, input, output):
		logger.info("DataStoreSmmServer.get_application_config()")
		#--- request ---
		param = input.u32()
		response = self.get_application_config(context, param)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.u32)
	
	def handle_set_application_config(self, context, input, output):
		logger.warning("DataStoreSmmServer.set_application_config is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_delete_application_config(self, context, input, output):
		logger.warning("DataStoreSmmServer.delete_application_config is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_latest_course_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.latest_course_search_object()")
		#--- request ---
		unknown1 = input.extract(UnknownStruct7)
		unknown2 = input.list(input.string)
		response = self.latest_course_search_object(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_followings_latest_course_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.followings_latest_course_search_object()")
		#--- request ---
		unknown1 = input.extract(UnknownStruct7)
		unknown2 = input.list(input.string)
		response = self.followings_latest_course_search_object(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_recommended_course_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.recommended_course_search_object()")
		#--- request ---
		unknown1 = input.extract(UnknownStruct7)
		unknown2 = input.list(input.string)
		response = self.recommended_course_search_object(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_score_range_cascaded_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.score_range_cascaded_search_object()")
		#--- request ---
		unknown1 = input.extract(UnknownStruct7)
		unknown2 = input.list(input.string)
		response = self.score_range_cascaded_search_object(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_suggested_course_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.suggested_course_search_object()")
		#--- request ---
		unknown1 = input.extract(UnknownStruct7)
		unknown2 = input.list(input.string)
		response = self.suggested_course_search_object(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_upload_course_record(self, context, input, output):
		logger.info("DataStoreSmmServer.upload_course_record()")
		#--- request ---
		param = input.extract(MethodParam71)
		self.upload_course_record(context, param)
	
	def handle_get_course_record(self, context, input, output):
		logger.info("DataStoreSmmServer.get_course_record()")
		#--- request ---
		param = input.extract(UnknownStruct2)
		response = self.get_course_record(context, param)
		
		#--- response ---
		if not isinstance(response, CourseRecordInfo):
			raise RuntimeError("Expected CourseRecordInfo, got %s" %response.__class__.__name__)
		output.add(response)
	
	def handle_delete_course_record(self, context, input, output):
		logger.warning("DataStoreSmmServer.delete_course_record is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_get_application_config_string(self, context, input, output):
		logger.info("DataStoreSmmServer.get_application_config_string()")
		#--- request ---
		param = input.u32()
		response = self.get_application_config_string(context, param)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.string)
	
	def handle_set_application_config_string(self, context, input, output):
		logger.warning("DataStoreSmmServer.set_application_config_string is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_get_deletion_reason(self, context, input, output):
		logger.info("DataStoreSmmServer.get_deletion_reason()")
		#--- request ---
		unknown = input.list(input.u64)
		response = self.get_deletion_reason(context, unknown)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.u32)
	
	def handle_set_deletion_reason(self, context, input, output):
		logger.warning("DataStoreSmmServer.set_deletion_reason is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_get_metas_with_course_record(self, context, input, output):
		logger.info("DataStoreSmmServer.get_metas_with_course_record()")
		#--- request ---
		unknown = input.list(UnknownStruct2)
		get_meta_param = input.extract(DataStoreGetMetaParam)
		response = self.get_metas_with_course_record(context, unknown, get_meta_param)
		
		#--- response ---
		if not isinstance(response, common.RMCResponse):
			raise RuntimeError("Expected RMCResponse, got %s" %response.__class__.__name__)
		for field in ['infos', 'unknown', 'results']:
			if not hasattr(response, field):
				raise RuntimeError("Missing field in RMCResponse: %s" %field)
		output.list(response.infos, output.add)
		output.list(response.unknown, output.add)
		output.list(response.results, output.result)
	
	def handle_check_rate_custom_ranking_counter(self, context, input, output):
		logger.info("DataStoreSmmServer.check_rate_custom_ranking_counter()")
		#--- request ---
		unk1 = input.u32()
		response = self.check_rate_custom_ranking_counter(context, unk1)
		
		#--- response ---
		if not isinstance(response, bool):
			raise RuntimeError("Expected bool, got %s" %response.__class__.__name__)
		output.bool(response)
	
	def handle_reset_rate_custom_ranking_counter(self, context, input, output):
		logger.warning("DataStoreSmmServer.reset_rate_custom_ranking_counter is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_best_score_rate_course_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.best_score_rate_course_search_object()")
		#--- request ---
		unknown1 = input.extract(UnknownStruct7)
		unknown2 = input.list(input.string)
		response = self.best_score_rate_course_search_object(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_ctr_pick_up_course_search_object(self, context, input, output):
		logger.info("DataStoreSmmServer.ctr_pick_up_course_search_object()")
		#--- request ---
		unknown1 = input.extract(UnknownStruct7)
		unknown2 = input.list(input.string)
		response = self.ctr_pick_up_course_search_object(context, unknown1, unknown2)
		
		#--- response ---
		if not isinstance(response, list):
			raise RuntimeError("Expected list, got %s" %response.__class__.__name__)
		output.list(response, output.add)
	
	def handle_search_unknown_platform_objects(self, context, input, output):
		logger.warning("DataStoreSmmServer.search_unknown_platform_objects is unsupported")
		raise common.RMCError("Core::NotImplemented")
	
	def handle_report_course(self, context, input, output):
		logger.info("DataStoreSmmServer.report_course()")
		#--- request ---
		param = input.extract(MethodParam87)
		self.report_course(context, param)
	
	def get_meta(self, *args):
		logger.warning("DataStoreSmmServer.get_meta not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def prepare_post_object(self, *args):
		logger.warning("DataStoreSmmServer.prepare_post_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def prepare_get_object(self, *args):
		logger.warning("DataStoreSmmServer.prepare_get_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def complete_post_object(self, *args):
		logger.warning("DataStoreSmmServer.complete_post_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_metas_multiple_param(self, *args):
		logger.warning("DataStoreSmmServer.get_metas_multiple_param not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def change_meta(self, *args):
		logger.warning("DataStoreSmmServer.change_meta not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def rate_objects(self, *args):
		logger.warning("DataStoreSmmServer.rate_objects not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_file_server_object_infos(self, *args):
		logger.warning("DataStoreSmmServer.get_file_server_object_infos not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def rate_custom_ranking(self, *args):
		logger.warning("DataStoreSmmServer.rate_custom_ranking not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def method49(self, *args):
		logger.warning("DataStoreSmmServer.method49 not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_custom_ranking_by_data_id(self, *args):
		logger.warning("DataStoreSmmServer.get_custom_ranking_by_data_id not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def add_to_buffer_queues(self, *args):
		logger.warning("DataStoreSmmServer.add_to_buffer_queues not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_buffer_queue(self, *args):
		logger.warning("DataStoreSmmServer.get_buffer_queue not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def complete_attach_file(self, *args):
		logger.warning("DataStoreSmmServer.complete_attach_file not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def prepare_attach_file(self, *args):
		logger.warning("DataStoreSmmServer.prepare_attach_file not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def conditional_search_object(self, *args):
		logger.warning("DataStoreSmmServer.conditional_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_application_config(self, *args):
		logger.warning("DataStoreSmmServer.get_application_config not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def latest_course_search_object(self, *args):
		logger.warning("DataStoreSmmServer.latest_course_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def followings_latest_course_search_object(self, *args):
		logger.warning("DataStoreSmmServer.followings_latest_course_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def recommended_course_search_object(self, *args):
		logger.warning("DataStoreSmmServer.recommended_course_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def score_range_cascaded_search_object(self, *args):
		logger.warning("DataStoreSmmServer.score_range_cascaded_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def suggested_course_search_object(self, *args):
		logger.warning("DataStoreSmmServer.suggested_course_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def upload_course_record(self, *args):
		logger.warning("DataStoreSmmServer.upload_course_record not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_course_record(self, *args):
		logger.warning("DataStoreSmmServer.get_course_record not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_application_config_string(self, *args):
		logger.warning("DataStoreSmmServer.get_application_config_string not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_deletion_reason(self, *args):
		logger.warning("DataStoreSmmServer.get_deletion_reason not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def get_metas_with_course_record(self, *args):
		logger.warning("DataStoreSmmServer.get_metas_with_course_record not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def check_rate_custom_ranking_counter(self, *args):
		logger.warning("DataStoreSmmServer.check_rate_custom_ranking_counter not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def best_score_rate_course_search_object(self, *args):
		logger.warning("DataStoreSmmServer.best_score_rate_course_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def ctr_pick_up_course_search_object(self, *args):
		logger.warning("DataStoreSmmServer.ctr_pick_up_course_search_object not implemented")
		raise common.RMCError("Core::NotImplemented")
	
	def report_course(self, *args):
		logger.warning("DataStoreSmmServer.report_course not implemented")
		raise common.RMCError("Core::NotImplemented")

