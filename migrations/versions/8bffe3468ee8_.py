"""empty message

Revision ID: 8bffe3468ee8
Revises: cc09c4e061d4
Create Date: 2021-05-06 01:10:11.867227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bffe3468ee8'
down_revision = 'cc09c4e061d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pw', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('birthday', sa.String(length=10), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userinfo')
    # ### end Alembic commands ###