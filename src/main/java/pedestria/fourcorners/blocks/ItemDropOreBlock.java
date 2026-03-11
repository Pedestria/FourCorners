package pedestria.fourcorners.blocks;

import java.util.Random;

import net.minecraft.block.material.Material;
import net.minecraft.block.state.IBlockState;
import net.minecraft.item.Item;

public class ItemDropOreBlock extends BlocksBase {
	
	Item itemDropped;

	public ItemDropOreBlock(String name, Material material, Item toDrop) {
		super(name, material);
		this.itemDropped = toDrop;
		// TODO Auto-generated constructor stub
	}


	@Override
	public Item getItemDropped(IBlockState state, Random random, int i) {

		return itemDropped;
	}

}
