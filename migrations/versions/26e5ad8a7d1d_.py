"""empty message

Revision ID: 26e5ad8a7d1d
Revises: 9b30a907767b
Create Date: 2018-09-06 11:17:44.418510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26e5ad8a7d1d'
down_revision = '9b30a907767b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('locale', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'locale')
    # ### end Alembic commands ###
