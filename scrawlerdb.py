import sqlalchemy
from sqlalchemy import Column,Integer,String
from scrawler1 import javajob
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import jinja2

Base = declarative_base()
class Java_Jobs(Base):
	__tablename__='javajobs'
	job_no=Column(Integer ,primary_key=True)
	designation=Column(String(1000))
	comp_name = Column(String(1000))
	experience= Column(String(500))
	location = Column(String(500))
	about_comp = Column(String(10000))

engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost')
engine.execute("USE scrawlerDB;")

Base.metadata.create_all(engine)
#engine.execute("create table javajobs(job_no varchar(10),designation varchar(200),comp_name varchar(200), experience varchar(50),location varchar(50), about_comp text )")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session=DBSession()


for i in javajob:
	#i = {k: i[k].encode('utf-8') for k in i.keys() if isinstance(i[k], basestring)}
	jj=Java_Jobs(job_no=i['count'],designation=i['designation'],comp_name=i['company_name'],experience =i['experience'],location=i['location'],about_comp=i['comp_descr'].encode('utf-8'))
	session.add(jj)
session.commit()	

#gives address wherever data is stored and query() returns a list.
result=session.query(Java_Jobs).all()

out=[]
for r in range(len(result)):
	temp=[]
	temp.append(result[r].job_no)
	temp.append(result[r].designation)
	temp.append(result[r].comp_name)
	temp.append(result[r].experience)
	temp.append(result[r].location)
	temp.append(result[r].about_comp.decode('utf-8'))
	out.append(temp)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
templ = templateEnv.get_template('view.html')
message= templ.render({'params':out})


# def insertion():
# 	for i in javajob:
# 		job_no=i['count']
# 		desig=i['designation']
# 		comp_name=i['company_name']
# 		experience =i['experience']
# 		location=i['location']
# 		detail=i['comp_descr']
# 		engine.execute("insert into javajobs values('%s','%s','%s','%s','%s','%s')" %(job_no,desig,comp_name,experience,location,detail))
		

# print insertion()
