"""buat tabel administator

Revision ID: 41f91ee65b70
Revises: 37110d49075e
Create Date: 2023-09-13 02:32:21.099217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41f91ee65b70'
down_revision = '37110d49075e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administator',
    sa.Column('ID_Admin', sa.BigInteger(), autoincrement=True, nullable=True),
    sa.Column('NIK', sa.BigInteger(), nullable=False),
    sa.Column('Nama', sa.String(length=20), nullable=False),
    sa.Column('Username', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('NIK')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('administator')
    # ### end Alembic commands ###
