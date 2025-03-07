"""empty message

Revision ID: 22990f0bc9f1
Revises: 52c1bf15cdda
Create Date: 2022-03-01 15:39:02.178762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22990f0bc9f1'
down_revision = '52c1bf15cdda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
