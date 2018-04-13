"""initial migration

Revision ID: 9f76c7aa0658
Revises: 
Create Date: 2018-04-12 18:47:02.027738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f76c7aa0658'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facter_architecture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('architecture', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_macaddress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('macaddress', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_manufacturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_processor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('processor0', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_productname',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_version',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('facterversion', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_virtual',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('virtual', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sshkey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pub', sa.String(length=2048), nullable=True),
    sa.Column('priv', sa.String(length=8192), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('vpnkey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crt', sa.String(length=8192), nullable=True),
    sa.Column('pvt_key', sa.String(length=4096), nullable=True),
    sa.Column('revoked', sa.Boolean(), nullable=True),
    sa.Column('blocked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facter_facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_virtual', sa.Boolean(), nullable=True),
    sa.Column('serialnumber', sa.String(length=128), nullable=True),
    sa.Column('uuid', sa.String(length=128), nullable=True),
    sa.Column('physicalprocessorcount', sa.Integer(), nullable=True),
    sa.Column('processorcount', sa.Integer(), nullable=True),
    sa.Column('memorysize', sa.String(length=32), nullable=True),
    sa.Column('memorysize_mb', sa.String(length=32), nullable=True),
    sa.Column('blockdevice_sda_size', sa.String(length=32), nullable=True),
    sa.Column('facterversion_id', sa.Integer(), nullable=True),
    sa.Column('architecture_id', sa.Integer(), nullable=True),
    sa.Column('virtual_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.Column('productname_id', sa.Integer(), nullable=True),
    sa.Column('processor_id', sa.Integer(), nullable=True),
    sa.Column('facter_json', sa.Text(length=65536), nullable=True),
    sa.ForeignKeyConstraint(['architecture_id'], ['facter_architecture.id'], ),
    sa.ForeignKeyConstraint(['facterversion_id'], ['facter_version.id'], ),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['facter_manufacturer.id'], ),
    sa.ForeignKeyConstraint(['processor_id'], ['facter_processor.id'], ),
    sa.ForeignKeyConstraint(['productname_id'], ['facter_productname.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['facter_type.id'], ),
    sa.ForeignKeyConstraint(['virtual_id'], ['facter_virtual.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_facter_facts_is_virtual'), 'facter_facts', ['is_virtual'], unique=False)
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('facter_facts__macaddress',
    sa.Column('macaddress_id', sa.Integer(), nullable=True),
    sa.Column('facts_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['facts_id'], ['facter_facts.id'], ),
    sa.ForeignKeyConstraint(['macaddress_id'], ['facter_macaddress.id'], )
    )
    op.create_table('server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=32), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('last_ping', sa.DateTime(), nullable=True),
    sa.Column('servername', sa.String(length=32), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('facter_facts_id', sa.Integer(), nullable=True),
    sa.Column('sshkey_id', sa.Integer(), nullable=True),
    sa.Column('vpnkey_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['facter_facts_id'], ['facter_facts.id'], ),
    sa.ForeignKeyConstraint(['sshkey_id'], ['sshkey.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vpnkey_id'], ['vpnkey.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_server_created'), 'server', ['created'], unique=False)
    op.create_index(op.f('ix_server_last_ping'), 'server', ['last_ping'], unique=False)
    op.create_index(op.f('ix_server_uuid'), 'server', ['uuid'], unique=False)
    op.create_table('activation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('last_ping', sa.DateTime(), nullable=True),
    sa.Column('activation_pin', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['server.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_activation_active'), 'activation', ['active'], unique=False)
    op.create_index(op.f('ix_activation_created'), 'activation', ['created'], unique=False)
    op.create_index(op.f('ix_activation_last_ping'), 'activation', ['last_ping'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_activation_last_ping'), table_name='activation')
    op.drop_index(op.f('ix_activation_created'), table_name='activation')
    op.drop_index(op.f('ix_activation_active'), table_name='activation')
    op.drop_table('activation')
    op.drop_index(op.f('ix_server_uuid'), table_name='server')
    op.drop_index(op.f('ix_server_last_ping'), table_name='server')
    op.drop_index(op.f('ix_server_created'), table_name='server')
    op.drop_table('server')
    op.drop_table('facter_facts__macaddress')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('followers')
    op.drop_index(op.f('ix_facter_facts_is_virtual'), table_name='facter_facts')
    op.drop_table('facter_facts')
    op.drop_table('vpnkey')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('sshkey')
    op.drop_table('facter_virtual')
    op.drop_table('facter_version')
    op.drop_table('facter_type')
    op.drop_table('facter_productname')
    op.drop_table('facter_processor')
    op.drop_table('facter_manufacturer')
    op.drop_table('facter_macaddress')
    op.drop_table('facter_architecture')
    # ### end Alembic commands ###