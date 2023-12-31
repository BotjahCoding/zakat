"""buat tabel staf

Revision ID: b2a143531281
Revises: 2cf20793a788
Create Date: 2023-09-13 03:25:51.140131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2a143531281'
down_revision = '2cf20793a788'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staf',
    sa.Column('NIK', sa.String(length=16), nullable=False),
    sa.Column('Nama', sa.String(length=50), nullable=False),
    sa.Column('Email', sa.String(length=50), nullable=False),
    sa.Column('Nomor_HP', sa.String(length=13), nullable=False),
    sa.Column('Username', sa.String(length=20), nullable=False),
    sa.Column('Password', sa.String(length=20), nullable=False),
    sa.Column('Kecamatan', sa.String(length=20), nullable=False),
    sa.Column('Gampong', sa.String(length=15), nullable=False),
    sa.Column('Kode_Gampong', sa.String(length=5), nullable=False),
    sa.Column('Dusun', sa.String(length=15), nullable=False),
    sa.Column('Admin', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['Admin'], ['admin.ID_Admin'], ),
    sa.PrimaryKeyConstraint('NIK')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('staf')
    # ### end Alembic commands ###
