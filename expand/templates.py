"""
	设置参数为索引值
		index=True

	假删除
		is_delete = db.Column(db.Boolean, default=False)

	事务:
		flush: 写数据库，但不提交，也就是事务未结束
		commit: 是先调用flush写数据库，然后提交，结束事务，并开始新的事务
		flush之后你才能在这个Session中看到效果，而commit之后你才能从其它Session中看到效果
		db.session.add(mapping)
		db.session.flush()
		db.session.commit()

"""

# 获取列表
def QueryExpand(request):
	"""查询

	Returns:
		total: 条目数
		result: 列表
		currentPage: 当前页数
		pageCount: 总页数
	"""
	querypage = request.get('querypage',1)
	pagesize = request.get('pagesize',10)

	# 过滤条件
	querys = 数据类.query.filter()

	# 排序
	querys = querys.order_by(数据类.create_time.desc())

	# 分页
	total, result, currentPage, pageCount = _Paginate(querys, querypage, pagesize)

	return 200, "", {
		"total":total,
		"result":[i.toDict() for i in result],
		"currentPage":currentPage,
		"pageCount":pageCount
	}

# 新增或编辑
def AddorEidt(request):
	"""新增或编辑

	Args:
		id (int): 数据id, 有id时为编辑 无id时为新增

	Returns:
		200 (int): 成功
		400 (int): 失败
		
	"""
	id = request.get('id',None)
	name = request.get('name',None)

	if not name:
		return 400, "参数不能为空", {}

	if id:
		obj = 数据类.query.get(id)
		if not obj:
			return 400, "被编辑的对象不存在", {}

	else:
		obj = 数据类()

	obj.name = name
	return obj._update()

# 操作
def Manager(request):
	"""[summary]

	Args:
		id (int): 要操作的数据id
		fucode (int): 功能码

	Doc:
		fucode:
			1: 删除

	Returns:
		200 (int): 成功
		400 (int): 失败

	"""
    id = request.get('id',None)
    fucode = request.get('fucode',None)

    if not all([id, fucode]):
        return 400, "参数有误", {}

    obj = 数据类.query.get(id)

    if not obj:
        return 400, "操作对象不存在", {}

    if fucode == 1:

        db.session.delete(obj)
        db.session.commit()
        return 200, "删除成功", {}