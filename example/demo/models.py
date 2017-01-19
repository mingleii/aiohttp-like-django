import datetime
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType

from aiohttp_like_django.models import ModelBase


PROXY_IP_STATUS = (
    (-1, "失效"),
    (0, "待验证"),
    (1, "有效"),
)


class ProxyIP(ModelBase):
    __tablename__ = "proxy_ip"

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    status = sa.Column(ChoiceType(PROXY_IP_STATUS, sa.SmallInteger()),
                       server_default="0")
    ip = sa.Column(sa.String(15), nullable=False)
    port = sa.Column(sa.String(10), nullable=False)
    area = sa.Column(sa.String(36), server_default="null")
    full_area = sa.Column(sa.String(36))
    anonymity = sa.Column(sa.String(8), server_default="null")
    protocol = sa.Column(sa.String(8), server_default="http")
    speed = sa.Column(sa.SmallInteger, server_default="-1")
    ctime = sa.Column(sa.DateTime(timezone=True), server_default=sa.func.now())
    utime = sa.Column(sa.DateTime, server_default=sa.func.now())
    __table_args__ = (sa.UniqueConstraint('ip', 'port',
                                          name="unique_ip_and_port"),)


sa_proxyip = ProxyIP.__table__  # type: sa.Table


class Question(ModelBase):
    __tablename__ = "question"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(36), nullable=False)
    question_text = sa.Column(sa.String(200), nullable=False)
    pub_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    choice = relationship("Choice", backref='user_ref')

sa_question = Question.__table__  # type: sa.Table


class Choice(ModelBase):
    __tablename__ = "choice"

    id = sa.Column(sa.Integer, primary_key=True)
    question_id = sa.Column(sa.Integer, sa.ForeignKey("question.id"),
                            nullable=False)
    choice_text = sa.Column(sa.String(200), nullable=False)
    votes = sa.Column(sa.Integer, server_default="0", nullable=False)

sa_choice = Choice.__table__  # type: sa.Table


class DemoTest(ModelBase):
    __tablename__ = "demo_test"

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(200), nullable=False, unique=True)

sa_demo_test = DemoTest.__table__  # type: sa.Table
