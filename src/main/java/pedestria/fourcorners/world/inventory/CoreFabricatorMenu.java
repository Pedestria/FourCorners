package pedestria.fourcorners.world.inventory;

import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.world.entity.player.Inventory;
import net.minecraftforge.items.SlotItemHandler;
import pedestria.fourcorners.registry.FCMenus;
import pedestria.fourcorners.world.level.block.entity.CoreFabricatorBlockEntity;
import pedestria.fourcorners.world.inventory.slot.OutputSlot;

public final class CoreFabricatorMenu extends FCMenuBase<CoreFabricatorBlockEntity> {
    public CoreFabricatorMenu(int containerId, Inventory inventory, CoreFabricatorBlockEntity blockEntity) {
        super(FCMenus.CORE_FABRICATOR_MENU.get(), containerId, inventory, blockEntity);

        addSlot(new OutputSlot(blockEntity.getItemHandler(), 9, 134, 59));
        for (int row = 0; row < 3; row++) {
            for (int column = 0; column < 3; column++) {
                addSlot(new SlotItemHandler(blockEntity.getItemHandler(), column + row * 3, 62 + column * 18, 23 + row * 18));
            }
        }

        addPlayerInventory(inventory, 8, 84);
    }

    public static CoreFabricatorMenu fromNetwork(
            int containerId, Inventory inventory, FriendlyByteBuf buffer) {
        return new CoreFabricatorMenu(
                containerId,
                inventory,
                blockEntityFromNetwork(inventory, buffer, CoreFabricatorBlockEntity.class));
    }

    @Override
    protected int getMachineSlotCount() {
        return 10;
    }
}
