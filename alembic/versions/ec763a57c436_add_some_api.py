"""add some api

Revision ID: ec763a57c436
Revises: 396fd784fc2f
Create Date: 2021-01-31 14:26:18.705655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec763a57c436'
down_revision = '396fd784fc2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coupon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=True, comment='系统中小程序的id'),
    sa.Column('border', sa.String(), nullable=True, comment='便条'),
    sa.Column('desc', sa.String(), nullable=True, comment='描述'),
    sa.Column('icon', sa.String(), nullable=True, comment='icon'),
    sa.Column('appid', sa.String(), nullable=True, comment='需要跳转的小程序的appid'),
    sa.Column('path', sa.String(), nullable=True, comment='跳转小程序的路径'),
    sa.Column('name', sa.String(), nullable=True, comment='cps名称'),
    sa.Column('platform', sa.String(), nullable=True, comment='平台'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序位置'),
    sa.Column('tip', sa.String(), nullable=True, comment='提示'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_coupon_app_id'), 'coupon', ['app_id'], unique=False)
    op.create_table('miniappad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=True, comment='系统中小程序的id'),
    sa.Column('ad_id', sa.String(), nullable=True, comment='申请到的广告id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_miniappad_app_id'), 'miniappad', ['app_id'], unique=False)
    op.create_table('miniapptip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=True, comment='系统中小程序的id'),
    sa.Column('tip', sa.String(), nullable=True, comment='提示'),
    sa.Column('page', sa.String(), nullable=True, comment='提示所在的页面'),
    sa.Column('item_id', sa.Integer(), nullable=True, comment='页面项目id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_miniapptip_app_id'), 'miniapptip', ['app_id'], unique=False)
    op.create_table('redcover',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=True, comment='系统中小程序的id'),
    sa.Column('receive_desc', sa.String(), nullable=True, comment='领取提示'),
    sa.Column('invite_limit', sa.Integer(), nullable=True, comment='领取的时候邀请用户的限制'),
    sa.Column('is_free', sa.Boolean(), nullable=True, comment='是否免费'),
    sa.Column('ad_limit', sa.Integer(), nullable=True, comment='领取是观看广告数的限制'),
    sa.Column('pic', sa.String(), nullable=True, comment='封面预览图'),
    sa.Column('is_task_together', sa.Boolean(), nullable=True, comment='是否需要同时完成两个任务'),
    sa.Column('is_in_stock', sa.Boolean(), nullable=True, comment='活动是否还在进行'),
    sa.Column('notice_show', sa.Boolean(), nullable=True, comment='是否展示通知'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_redcover_app_id'), 'redcover', ['app_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_redcover_app_id'), table_name='redcover')
    op.drop_table('redcover')
    op.drop_index(op.f('ix_miniapptip_app_id'), table_name='miniapptip')
    op.drop_table('miniapptip')
    op.drop_index(op.f('ix_miniappad_app_id'), table_name='miniappad')
    op.drop_table('miniappad')
    op.drop_index(op.f('ix_coupon_app_id'), table_name='coupon')
    op.drop_table('coupon')
    # ### end Alembic commands ###
