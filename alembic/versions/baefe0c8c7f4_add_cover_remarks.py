"""add cover remarks

Revision ID: baefe0c8c7f4
Revises: a34c65c94a46
Create Date: 2021-02-03 12:51:08.341135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baefe0c8c7f4'
down_revision = 'a34c65c94a46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('redcover', sa.Column('remarks', sa.String(), nullable=True, comment='备注'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('redcover', 'remarks')
    # ### end Alembic commands ###