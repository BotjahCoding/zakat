"""buat tabel administator

Revision ID: 116491a72022
Revises: 41f91ee65b70
Create Date: 2023-09-13 02:33:50.098652

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '116491a72022'
down_revision = '41f91ee65b70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('administator', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Password', sa.String(length=20), nullable=False))
        batch_op.alter_column('Nama',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('administator', schema=None) as batch_op:
        batch_op.alter_column('Nama',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.drop_column('Password')

    # ### end Alembic commands ###
