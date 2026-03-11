package pedestria.fourcorners.container;

import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.entity.player.InventoryPlayer;
import net.minecraft.inventory.Container;
import net.minecraft.inventory.Slot;
import net.minecraft.item.ItemStack;
import pedestria.fourcorners.api.IContainer;

public class ContainerMachineBase extends Container implements IContainer {

	public ContainerMachineBase() {
	}

	public void initPlayerInventory(InventoryPlayer inventoryPlayer) {
		// HOTBAR INVENTORY
		for (int i = 0; i < 9; i++) {
			addSlotToContainer(new Slot(inventoryPlayer, i, 8 + (i * 18), 142));
		}
		// MAIN PLAYER INVENTORY
		for (int y = 0; y < 3; y++) {
			for (int x = 0; x < 9; x++) {
				addSlotToContainer(new Slot(inventoryPlayer, x + (y * 9) + 9, 8 + x * 18, 84 + y * 18));
			}
		}

	}

	@Override
	public ItemStack transferStackInSlot(EntityPlayer player, int index) {
		ItemStack stack = ItemStack.EMPTY;
		Slot slot = inventorySlots.get(index);

		if (slot != null && slot.getHasStack()) {
			ItemStack stackInSlot = slot.getStack();
			stack = stackInSlot.copy();

			int containerSlots = inventorySlots.size() - player.inventory.mainInventory.size();

			if (index < containerSlots) {
				if (!this.mergeItemStack(stackInSlot, containerSlots, inventorySlots.size(), true)) {
					return ItemStack.EMPTY;
				}

			} else if (!this.mergeItemStack(stackInSlot, 0, containerSlots, false)) {
				return ItemStack.EMPTY;
			}

			if (stackInSlot.getCount() == 0) {
				slot.putStack(ItemStack.EMPTY);
			} else {
				slot.onSlotChanged();
			}

			slot.onTake(player, stackInSlot);
		}
		return stack;

	}

	@Override
	public boolean canInteractWith(EntityPlayer player) {

		return true;
	}
	
}
