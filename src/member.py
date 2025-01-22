import asyncio
import time
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors import UserPrivacyRestrictedError


# ---------------------------------------------------------------------
async def _add_members(api_id, api_hash, session_name):
    client = TelegramClient(session_name, api_id, api_hash)

    await client.start()

    try:
        source_group_username = input(
            "Enter the source group username: "
        ).strip()
        target_group_username = input(
            "Enter the target group username: "
        ).strip()

        source_group = await client.get_entity(source_group_username)
        target_group = await client.get_entity(target_group_username)

        source_group_id = source_group.id
        target_group_id = target_group.id

        # Get all participants of the source group
        participants = await client.get_participants(source_group_id)

        # Invite each participant to the target group
        for participant in participants:
            try:
                await client(
                    InviteToChannelRequest(target_group_id, [participant])
                )
                print(
                    f"Added {participant.id} "
                    f"({participant.username}) to target group"
                )
                time.sleep(3)

            except UserPrivacyRestrictedError:
                print(
                    f"Failed to add {participant.id} "
                    f"({participant.username}) due to privacy settings"
                )

            except Exception as e:
                print(
                    f"Failed to add {participant.id} "
                    f"({participant.username}): {e}"
                )

    finally:
        await client.disconnect()
        print("Finished adding members and disconnected the client.")


# ---------------------------------------------------------------------
async def main(api_id, api_hash, session_name):
    await _add_members(api_id, api_hash, session_name)


# ---------------------------------------------------------------------
def add_members(api_id, api_hash, session_name):
    asyncio.run(main(api_id, api_hash, session_name))
